from flask import Flask, jsonify, render_template
import cohere

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response')
def get_response():
    co = cohere.Client("ArnEDE2bVtFU63oba6ErCIGAmqnQ7I5rAEByHYAF")
    response = co.chat(message="hello world!")
    return jsonify({"text": response.text})

if __name__ == '__main__':
    app.run(debug=True)