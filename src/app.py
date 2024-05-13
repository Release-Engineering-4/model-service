from flask import Flask, request, jsonify
from flasgger import Swagger
from keras.models import load_model
import numpy as np

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/', methods=['POST'])
def show_swagger():
    """
    Make a hardcoded prediction
    ---
    consumes:
        - application/json
    parameters:
        - name: input_data
          in: body
          description: message to be classified.
          required: True
          schema:
          type: object
          required: sms
          properties:
            msg:
                type: string
                example: This is an example msg.
    responses:
        200:
            description: Some result
    """
    msg = request.get_json().get('msg')
    return {
    "result": "Message was: " + msg ,
    }


@app.route('/predict', methods=['POST'])
def predict():
    trained_model = load_model("models/trained_model.h5")
    data = request.get_json()
    input_data = np.array(data['input_data'])

    y_pred = trained_model.predict(input_data)
    y_pred_binary = (y_pred > 0.5).astype(int)

    return jsonify({'prediction': y_pred_binary})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)