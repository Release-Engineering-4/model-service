"""
Model wrapper
"""

from flask import Flask, request, jsonify
from flasgger import Swagger
import gdown
from keras.models import load_model
from remla_preprocess.pre_processing import MLPreprocessor
import numpy as np

gdown.download_folder(
    "https://drive.google.com/drive/folders/1bj2O4NW9yreSGa1NKd01HebZnJ6iH4Dl",
    output="models",
)

app = Flask(__name__)
swagger = Swagger(app)


@app.route("/predict", methods=["POST"])
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
    url_string = data["url"]
    processor = MLPreprocessor(200, "./models/tokenizer.pkl", None)
    trained_model = load_model("./models/trained_model.h5")
    processed_input = processor.tokenize_pad_data([url_string])
    prediction = trained_model.predict(processed_input)
    binary_prediction = (np.array(prediction) > 0.5).astype(int)

    prediction = prediction.tolist()
    binary_prediction = binary_prediction.tolist()

    return jsonify({"prediction_binary": binary_prediction,
                    "prediction": prediction})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
