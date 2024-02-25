from src.models.geoname_model import Geoname


def test_new_geoname():
    """
    GIVEN a Geoname model
    WHEN a new Geoname is created
    THEN check the name, latitude, longitude, country, population, elevation, and tz fields are defined correctly
    """
    geoname = Geoname(
        name='Oz',
        ascii_name='Oz',
        latitude=45.50884,
        longitude=-73.58781,
        country='ML',
        population=1600000,
        elevation=216,
        tz='America/Toronto'
    )
    assert geoname.name == 'Oz'
    assert geoname.latitude == 45.50884
    assert geoname.longitude == -73.58781
    assert geoname.country == 'ML'
    assert geoname.tz == 'America/Toronto'
    assert geoname.population == 1600000
    assert geoname.elevation == 216
