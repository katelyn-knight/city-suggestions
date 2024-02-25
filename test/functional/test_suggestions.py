
from functional import setup_app, setup_db


def test_suggestions_empty():
    """
    GIVEN a Flask application
    WHEN the '/suggestions' page is requested (GET) without a query parameter
    THEN check the response is 400 and the error message is returned
    """
    app = setup_app()

    from src.routes import suggestions
    app.register_blueprint(suggestions)

    with app.test_client() as client:
        response = client.get('/suggestions')
        assert response.status_code == 400
        assert response.data == b'{"error": "q parameter is required"}'


def test_suggestions_match_no_coord():
    """
    GIVEN a Flask application
    WHEN the '/suggestions' page is requested (GET) with a query parameter
    THEN check the response is 200
    """
    app = setup_app()
    db = setup_db(app)

    from src.routes import suggestions
    app.register_blueprint(suggestions)

    with app.test_client() as client:
        response = client.get('/suggestions?q=London')
        assert response.status_code == 200


def test_suggestions_match_with_coord():
    """
    GIVEN a Flask application
    WHEN the '/suggestions' page is requested (GET) with a query parameter and coordinates
    THEN check the response is 200 and the expected data is returned
    """
    app = setup_app()
    db = setup_db(app)

    from src.routes import suggestions
    app.register_blueprint(suggestions)

    with app.test_client() as client:
        response = client.get('/suggestions?q=Londn&latitude=43.70011&longitude=-79.4163')
        assert response.status_code == 200
        assert response.data == b'{"suggestions": [{"latitude": 42.98339, "longitude": -81.23304, "name": "London, ' \
                                b'08, CA", "score": 0.9886679613949874}, {"latitude": 42.46676, "longitude": ' \
                                b'-70.94949, "name": "Lynn, MA, US", "score": 0.9393256837984394}, {"latitude": ' \
                                b'42.44613, "longitude": -87.83285, "name": "Zion, IL, US", ' \
                                b'"score": 0.8211372338192395}, {"latitude": 36.39559, "longitude": -97.87839, ' \
                                b'"name": "Enid, OK, US", "score": 0.8146416108812473}, {"latitude": 38.8906, ' \
                                b'"longitude": -90.18428, "name": "Alton, IL, US", "score": 0.8107064614719819}, ' \
                                b'{"latitude": 41.223, "longitude": -111.97383, "name": "Ogden, UT, US", ' \
                                b'"score": 0.7928144356453379}, {"latitude": 36.48847, "longitude": -79.7667, ' \
                                b'"name": "Eden, NC, US", "score": 0.761382344864556}, {"latitude": 41.73549, ' \
                                b'"longitude": -111.83439, "name": "Logan, UT, US", "score": 0.7420242622945368}, ' \
                                b'{"latitude": 39.76282, "longitude": -86.39972, "name": "Avon, IN, US", ' \
                                b'"score": 0.7402600621878088}, {"latitude": 44.05817, "longitude": -121.31531, ' \
                                b'"name": "Bend, OR, US", "score": 0.7353196969112404}, {"latitude": 34.77453, ' \
                                b'"longitude": -96.67834, "name": "Ada, OK, US", "score": 0.7212918897221845}, ' \
                                b'{"latitude": 41.16161, "longitude": -112.02633, "name": "Roy, UT, US", ' \
                                b'"score": 0.7134471992829241}, {"latitude": 38.1302, "longitude": -121.27245, ' \
                                b'"name": "Lodi, CA, US", "score": 0.7078431008228043}, {"latitude": 38.25674, ' \
                                b'"longitude": -85.60163, "name": "Lyndon, KY, US", "score": 0.6959629154296059}, ' \
                                b'{"latitude": 41.81337, "longitude": -87.81811, "name": "Lyons, IL, US", ' \
                                b'"score": 0.6882321883833713}, {"latitude": 39.18589, "longitude": -84.65134, ' \
                                b'"name": "Dent, OH, US", "score": 0.6786086362967221}, {"latitude": 26.52036, ' \
                                b'"longitude": -81.96398, "name": "Iona, FL, US", "score": 0.6721787786582365}, ' \
                                b'{"latitude": 39.88645, "longitude": -83.44825, "name": "London, OH, US", ' \
                                b'"score": 0.6607686943697941}, {"latitude": 40.83242, "longitude": -115.76312, ' \
                                b'"name": "Elko, NV, US", "score": 0.6529618787832112}, {"latitude": 36.10291, ' \
                                b'"longitude": -79.50669, "name": "Elon, NC, US", "score": 0.6269316115100918}, ' \
                                b'{"latitude": 32.7559, "longitude": -111.55484, "name": "Eloy, AZ, US", ' \
                                b'"score": 0.6231542042148246}, {"latitude": 35.30627, "longitude": -78.6089, ' \
                                b'"name": "Dunn, NC, US", "score": 0.6075969843877524}, {"latitude": 26.28729, ' \
                                b'"longitude": -98.31335, "name": "Alton, TX, US", "score": 0.6015183828930188}, ' \
                                b'{"latitude": 37.12898, "longitude": -84.08326, "name": "London, KY, US", ' \
                                b'"score": 0.5884405417206761}, {"latitude": 39.54007, "longitude": -82.4071, ' \
                                b'"name": "Logan, OH, US", "score": 0.5828214122477565}, {"latitude": 39.312, ' \
                                b'"longitude": -84.28299, "name": "Landen, OH, US", "score": 0.549116608762531}, ' \
                                b'{"latitude": 48.9465, "longitude": -122.45211, "name": "Lynden, WA, US", ' \
                                b'"score": 0.5387384691217633}, {"latitude": 40.34329, "longitude": -111.72076, ' \
                                b'"name": "Lindon, UT, US", "score": 0.5290037138549908}, {"latitude": 34.27239, ' \
                                b'"longitude": -77.81859, "name": "Ogden, NC, US", "score": 0.5072603275540158}, ' \
                                b'{"latitude": 29.34746, "longitude": -99.14142, "name": "Hondo, TX, US", ' \
                                b'"score": 0.4974528937089647}, {"latitude": 44.51422, "longitude": -72.01093, ' \
                                b'"name": "Lyndon, VT, US", "score": 0.48577495102525303}, {"latitude": 31.28267, ' \
                                b'"longitude": -86.25551, "name": "Opp, AL, US", "score": 0.4637158981533666}, ' \
                                b'{"latitude": 35.73285, "longitude": -84.33381, "name": "Loudon, TN, US", ' \
                                b'"score": 0.4466972481580449}, {"latitude": 51.78341, "longitude": -114.10199, ' \
                                b'"name": "Olds, 01, CA", "score": 0.42120098077118134}, {"latitude": 19.72972, ' \
                                b'"longitude": -155.09, "name": "Hilo, HI, US", "score": 0.40789473684210525}, ' \
                                b'{"latitude": 39.63137, "longitude": -106.52225, "name": "Avon, CO, US", ' \
                                b'"score": 0.39764922903154065}, {"latitude": 38.35269, "longitude": -120.93272, ' \
                                b'"name": "Ione, CA, US", "score": 0.39456647232836123}, {"latitude": 28.97859, ' \
                                b'"longitude": -96.64609, "name": "Edna, TX, US", "score": 0.38755552261828047}]} '


def test_suggestions_fuzzy_match():
    """
    GIVEN a Flask application
    WHEN the '/suggestions' page is requested (GET) with a misspelled query parameter
    THEN check the response is 200 and the response is a JSON object with the correct suggestions
    """
    app = setup_app()
    db = setup_db(app)

    from src.routes import suggestions
    app.register_blueprint(suggestions)

    with app.test_client() as client:
        response = client.get('/suggestions?q=Londn')
        assert response.status_code == 200
        assert response.data == b'{"suggestions": [{"latitude": 42.98339, "longitude": -81.23304, "name": "London, ' \
                                b'08, CA", "score": 1.0}, {"latitude": 42.46676, "longitude": -70.94949, ' \
                                b'"name": "Lynn, MA, US", "score": 0.9736842105263158}, {"latitude": 41.223, ' \
                                b'"longitude": -111.97383, "name": "Ogden, UT, US", "score": 0.9473684210526316}, ' \
                                b'{"latitude": 44.05817, "longitude": -121.31531, "name": "Bend, OR, US", ' \
                                b'"score": 0.9210526315789473}, {"latitude": 38.1302, "longitude": -121.27245, ' \
                                b'"name": "Lodi, CA, US", "score": 0.8947368421052632}, {"latitude": 36.39559, ' \
                                b'"longitude": -97.87839, "name": "Enid, OK, US", "score": 0.868421052631579}, ' \
                                b'{"latitude": 41.73549, "longitude": -111.83439, "name": "Logan, UT, US", ' \
                                b'"score": 0.8421052631578947}, {"latitude": 19.72972, "longitude": -155.09, ' \
                                b'"name": "Hilo, HI, US", "score": 0.8157894736842105}, {"latitude": 41.16161, ' \
                                b'"longitude": -112.02633, "name": "Roy, UT, US", "score": 0.7894736842105263}, ' \
                                b'{"latitude": 38.8906, "longitude": -90.18428, "name": "Alton, IL, US", ' \
                                b'"score": 0.7631578947368421}, {"latitude": 42.44613, "longitude": -87.83285, ' \
                                b'"name": "Zion, IL, US", "score": 0.736842105263158}, {"latitude": 40.83242, ' \
                                b'"longitude": -115.76312, "name": "Elko, NV, US", "score": 0.7105263157894737}, ' \
                                b'{"latitude": 34.77453, "longitude": -96.67834, "name": "Ada, OK, US", ' \
                                b'"score": 0.6842105263157895}, {"latitude": 32.7559, "longitude": -111.55484, ' \
                                b'"name": "Eloy, AZ, US", "score": 0.6578947368421053}, {"latitude": 36.48847, ' \
                                b'"longitude": -79.7667, "name": "Eden, NC, US", "score": 0.631578947368421}, ' \
                                b'{"latitude": 26.52036, "longitude": -81.96398, "name": "Iona, FL, US", ' \
                                b'"score": 0.6052631578947368}, {"latitude": 39.76282, "longitude": -86.39972, ' \
                                b'"name": "Avon, IN, US", "score": 0.5789473684210527}, {"latitude": 26.28729, ' \
                                b'"longitude": -98.31335, "name": "Alton, TX, US", "score": 0.5526315789473685}, ' \
                                b'{"latitude": 48.9465, "longitude": -122.45211, "name": "Lynden, WA, US", ' \
                                b'"score": 0.5263157894736843}, {"latitude": 38.25674, "longitude": -85.60163, ' \
                                b'"name": "Lyndon, KY, US", "score": 0.5}, {"latitude": 41.81337, "longitude": ' \
                                b'-87.81811, "name": "Lyons, IL, US", "score": 0.4736842105263158}, {"latitude": ' \
                                b'39.18589, "longitude": -84.65134, "name": "Dent, OH, US", ' \
                                b'"score": 0.44736842105263164}, {"latitude": 40.34329, "longitude": -111.72076, ' \
                                b'"name": "Lindon, UT, US", "score": 0.42105263157894735}, {"latitude": 39.88645, ' \
                                b'"longitude": -83.44825, "name": "London, OH, US", "score": 0.39473684210526316}, ' \
                                b'{"latitude": 36.10291, "longitude": -79.50669, "name": "Elon, NC, US", ' \
                                b'"score": 0.368421052631579}, {"latitude": 35.30627, "longitude": -78.6089, ' \
                                b'"name": "Dunn, NC, US", "score": 0.3421052631578948}, {"latitude": 29.34746, ' \
                                b'"longitude": -99.14142, "name": "Hondo, TX, US", "score": 0.3157894736842106}, ' \
                                b'{"latitude": 37.12898, "longitude": -84.08326, "name": "London, KY, US", ' \
                                b'"score": 0.2894736842105263}, {"latitude": 38.35269, "longitude": -120.93272, ' \
                                b'"name": "Ione, CA, US", "score": 0.26315789473684215}, {"latitude": 39.54007, ' \
                                b'"longitude": -82.4071, "name": "Logan, OH, US", "score": 0.23684210526315796}, ' \
                                b'{"latitude": 51.78341, "longitude": -114.10199, "name": "Olds, 01, CA", ' \
                                b'"score": 0.21052631578947367}, {"latitude": 39.312, "longitude": -84.28299, ' \
                                b'"name": "Landen, OH, US", "score": 0.1842105263157895}, {"latitude": 34.27239, ' \
                                b'"longitude": -77.81859, "name": "Ogden, NC, US", "score": 0.1578947368421053}, ' \
                                b'{"latitude": 31.28267, "longitude": -86.25551, "name": "Opp, AL, US", ' \
                                b'"score": 0.13157894736842113}, {"latitude": 39.63137, "longitude": -106.52225, ' \
                                b'"name": "Avon, CO, US", "score": 0.10526315789473695}, {"latitude": 28.97859, ' \
                                b'"longitude": -96.64609, "name": "Edna, TX, US", "score": 0.07894736842105265}, ' \
                                b'{"latitude": 44.51422, "longitude": -72.01093, "name": "Lyndon, VT, US", ' \
                                b'"score": 0.052631578947368474}, {"latitude": 35.73285, "longitude": -84.33381, ' \
                                b'"name": "Loudon, TN, US", "score": 0.026315789473684292}]} '


def test_suggestions_no_match():
    """
    GIVEN a Flask application
    WHEN the '/suggestions' page is requested (GET) with a single character query string
    THEN check the response is 200 and the response is an empty list
    """
    app = setup_app()
    db = setup_db(app)

    from src.routes import suggestions
    app.register_blueprint(suggestions)

    with app.test_client() as client:
        response = client.get('suggestions?q=L')
        assert response.status_code == 200
        assert response.data == b'{"suggestions": []}'
        assert response.content_type == 'application/json'
