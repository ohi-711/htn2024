from flask import Flask, request, jsonify, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    data = request.json
    response = f"You said: {data['message']}"
    return jsonify({"text": response})

@app.route('/run_script', methods=['POST'])
def run_script():
    try:
        result = subprocess.run(['python', 'automate_post.py'], capture_output=True, text=True, check=True)
        output = result.stdout
        return jsonify({"output": output})
    except subprocess.CalledProcessError as e:
        return jsonify({"error": str(e), "output": e.output}), 500

if __name__ == '__main__':
    app.run(debug=True)