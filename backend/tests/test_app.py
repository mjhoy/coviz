def test_health_check(backend_api_client):
    response = backend_api_client.get("/")
    assert response.status_code == 200
