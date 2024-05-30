from model_service.app import app

SAMPLE_URL = "https://sample_url.com"


def test_response():
    with app.test_client() as c:
        response = c.post('/predict', json={"url": SAMPLE_URL})
        # Check if the response code is correct
        assert response.status_code == 200


def test_keys():
    with app.test_client() as c:
        response = c.post('/predict', json={"url": SAMPLE_URL})
        # Check if keys are correct
        assert response.json.keys() == {"prediction_binary", "prediction"}


def test_prediction_binary():
    with app.test_client() as c:
        response = c.post('/predict', json={"url": SAMPLE_URL})
        # Check if values are correct
        assert isinstance(response.json["prediction_binary"][0][0], int)


def test_prediction():
    with app.test_client() as c:
        response = c.post('/predict', json={"url": SAMPLE_URL})
        # Check if values are correct
        assert isinstance(response.json["prediction"][0][0], float)

