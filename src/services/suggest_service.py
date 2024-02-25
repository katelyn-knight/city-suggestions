from flask import jsonify
from src.models.geoname_model import Geoname
from math import radians, sin, cos, sqrt, atan2
from sqlalchemy import or_
from Levenshtein import distance as levenshtein_distance


def remove_duplicates(cities):
    unique_cities = []
    seen_city_attributes = set()
    for city in cities:
        city_attributes = (city.name, city.latitude, city.longitude)
        # Only add the city if its attributes haven't been seen before
        if city_attributes not in seen_city_attributes:
            unique_cities.append(city)
            seen_city_attributes.add(city_attributes)
    return unique_cities


def query_geoname_for_name(q):
    # Generate substrings of the query
    substrings = [q[i:j] for i in range(len(q)) for j in range(i + 1, len(q) + 1)]

    # Get all cities whose name exactly matches or is a partial match to any substring
    list_cities = Geoname.query.filter(or_(
        Geoname.name == q,
        Geoname.name.like('%' + q + '%'),
        Geoname.name.ilike('%' + q + '%'),  # Case-insensitive match
        *[
            Geoname.name.like('%' + substring + '%') for substring in substrings
        ]
    )).all()

    # Filter out near matches based on Levenshtein distance
    near_matches = []
    for city in list_cities:
        for substring in substrings:
            if levenshtein_distance(city.name.lower(), substring.lower()) <= 2:
                near_matches.append(city)
                break  # Once a match is found, break out of the inner loop

    return remove_duplicates(near_matches)


def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points
    on the earth specified in decimal degrees.
    """
    # Convert decimal degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = 6371 * c  # Radius of earth in kilometers
    return distance


class SuggestionsService:
    def __init__(self, lat, lon):
        # Check if latitude and longitude are provided
        if lat and lon:
            # Convert latitude and longitude to float
            self.lat = float(lat)
            self.lon = float(lon)
            self.coordinatesPresent = True
        else:
            self.coordinatesPresent = False

    def calculate_distance_weight(self, other_locations):
        # Calculate distances between the given location and other locations
        distances = {}
        max_distance = float('-inf')
        for location in other_locations:
            loc = location.to_dict()
            distance = haversine_distance(self.lat, self.lon, loc['latitude'], loc['longitude'])
            distances[loc['id']] = distance
            if distance > max_distance:
                max_distance = distance

        # Calculate weights based on distances
        weights = {}
        for location_id, distance in distances.items():
            weight = 1 - (distance / max_distance)
            weights[location_id] = weight

        return weights

    def calculate_population_weight(self, towns):
        # Calculate weights based on population
        population_weights = {}
        sorted_pop_desc = sorted(towns, key=lambda town: town.population, reverse=True)
        delta = 1/len(towns)
        for i, town in enumerate(sorted_pop_desc):
            population_weights[town.id] = 1 - (i * delta)
        return population_weights

    def calculate_score(self, cities):
        # Calculate the combined score based on distance and population
        if len(cities) > 1:
            if self.coordinatesPresent:
                distance_weights = self.calculate_distance_weight(cities)
                population_weights = self.calculate_population_weight(cities)
                combined_scores = {}
                for city_id in distance_weights.keys():
                    combined_score = (distance_weights[city_id] + population_weights[city_id]) / 2
                    combined_scores[city_id] = combined_score
            else:
                combined_scores = self.calculate_population_weight(cities)
        else:
            combined_scores = {cities[0].id: 1}
        return combined_scores

    def format_suggestions(self, cities):
        suggestions = []
        scores = self.calculate_score(cities)
        for city in cities:
            score = scores[city.id]
            pretty_city = city.to_dict()
            full_name = pretty_city['name'] + ', ' + pretty_city['admin1'] + ', ' + pretty_city['country']
            simplified_city = {
                "name": full_name,
                "latitude": pretty_city['latitude'],
                "longitude": pretty_city['longitude'],
                "score": score
            }
            suggestions.append(simplified_city)
        return suggestions

    def get_suggestions(self, q):
        # Suggest cities based on the query
        cities = query_geoname_for_name(q)
        if not cities:
            return []
        suggestions = self.format_suggestions(cities)
        sorted_suggestions = sorted(suggestions, key=lambda k: k['score'], reverse=True)
        return sorted_suggestions
