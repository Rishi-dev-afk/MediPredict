from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('disease_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Expecting a dictionary with these keys
    expected_keys = ['Age', 'Sex', 'ChestPainType', 'RestingBP', 'Cholesterol', 'FastingBS',
                     'RestingECG', 'MaxHR', 'ExerciseAngina', 'Oldpeak', 'ST_Slope']
    
    try:
        features = [data[key] for key in expected_keys]
        features = np.array(features).reshape(1, -1)
        prediction = model.predict(features)
        return jsonify({'prediction': int(prediction[0])})
    
    except KeyError as e:
        return jsonify({'error': f'Missing key: {str(e)}'}), 400

if __name__ == '__main__':
    app.run(debug=True)
