from test import client


def test_suggestion_empty(client):
    response = client.get('/suggestions')
    assert response.status_code == 400
    assert response.json == {'error': "Query parameter 'q' is required"}


def test_suggestion_montreal(client):
    response = client.get('/suggestions?q=montreal')
    assert response.status_code == 200
    assert response.json == {'suggestions': [{'name': 'Montreal, QC, Canada', 'latitude': '45.50884', 'longitude': '-73.58781', 'score': 0.9}]}