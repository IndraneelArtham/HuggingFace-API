from flask import Flask, request, jsonify
from transformers import pipeline

model = pipeline('sentiment-analysis')


app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        data = request.json
        text = data['text']
        result = model(text)
        return jsonify(result[0]['label'])

if __name__ == '__main__':
    app.run(debug=True)