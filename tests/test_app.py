from model_service.app import app

def test_predict():
    with app.test_client() as c:
        response = c.post('/predict', json={"url": "https://sample_url.com"})
        assert response.status_code == 200
        # The prediction values will change with each run, so we can't compare them directly.
        #assert response.json == {"prediction_binary": [0], "prediction": [[0.123]]}
        assert response.json.keys() == {"prediction_binary", "prediction"}