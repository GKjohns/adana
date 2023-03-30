from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Dummy language model function (replace with your actual language model function)
def language_model(prompt):
    return prompt[::-1]

@app.route('/api/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)
        prompt = data['prompt']
        response = language_model(prompt)

        return jsonify({
            'status': 'success',
            'response': response
        })

    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8881, debug=True)
