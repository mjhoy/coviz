def test_health_check(backend_api_client):
    response = backend_api_client.get("/")
    assert response.status_code == 200


def test_get_new_confirmed(backend_api_client):
    response = backend_api_client.get("/covid/confirmed/new/03-03-20")
    assert response.status_code == 200


def test_get_confirmed_to_date(backend_api_client):
    response = backend_api_client.get("/covid/confirmed/total/03-03-20")
    assert response.status_code == 200
