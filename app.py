from flask import Flask, request, jsonify
import numpy as np
from predict import predict

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    input_data = np.array(data['input'])
    
    prediction = predict(input_data)
    
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)