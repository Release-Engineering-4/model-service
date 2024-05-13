from flask import Flask, request, jsonify
from flasgger import Swagger
from keras.models import load_model
import numpy as np
from remla_preprocess.pre_processing import MLPreprocessor


app = Flask(__name__)
swagger = Swagger(app)

@app.route('/predict', methods=['POST'])
def predict():
    """
    Endpoint to predict URL Phishing.
    ---
    parameters:
      - name: url
        in: body
        required: true
        schema:
          type: object
          properties:
            url:
              type: string
              example: "https://sample_url.com"
    responses:
      200:
        description: A JSON object with the prediction.
        schema:
          type: object
          properties:
            prediction_binary:
              type: int
              example: 0
            prediction:
              type: float
              example: 0.123
    """
    data = request.get_json()
    url_string = data['url']
    print(url_string)
    input_data = MLPreprocessor().tokenize_pad_data([url_string])
    # TODO: Load model and predict from there
    # trained_model = load_model("models/trained_model.h5")
    # print("loaded model")

    # y_pred = trained_model.predict(input_data)
    y_pred = 0.74
    y_pred_binary = (y_pred > 0.5).astype(int)

    return jsonify({'prediction_binary': y_pred_binary, 'prediction': y_pred})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)