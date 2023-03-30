from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)   # eliminate the CORS error

dummy_text = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. In et leo at mi facilisis efficitur. Suspendisse non ultricies enim. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Integer auctor justo sit amet mi bibendum, eget fringilla dolor tempus. Etiam feugiat risus quam, ut auctor lorem tempor ac\nPhasellus ultricies turpis nisl, eget pretium nunc bibendum eu. Aenean vestibulum diam eget quam tincidunt ullamcorper. Cras maximus purus vel quam vulputate, nec gravida massa pellentesque. Pellentesque egestas mi ac metus fringilla, eu fringilla arcu accumsan. Integer finibus, metus in fermentum eleifend, nisl urna pharetra sapien, vitae sollicitudin ligula urna vitae orci.\nSed sit amet tincidunt justo. Suspendisse et sapien est. Cras ut urna vel justo cursus convallis eu in ipsum. Ut at vestibulum nunc. Aenean facilisis, felis ut rhoncus feugiat, quam mauris tempus orci, ut suscipit felis lectus sed purus. Sed venenatis risus vitae tortor commodo lacinia'''

# Dummy language model function (replace with your actual language model function)
def language_model(prompt):
    return prompt[::-1] + '>>>>' + dummy_text


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
