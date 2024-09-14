from flask import Flask, jsonify, render_template, request
import cohere

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/chat')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.json['message']
    co = cohere.Client("ArnEDE2bVtFU63oba6ErCIGAmqnQ7I5rAEByHYAF")
    response = co.chat(message=user_message)
    return jsonify({"text": response.text})

if __name__ == '__main__':
    app.run(debug=True)