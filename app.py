from flask import Flask, request, jsonify, render_template
import subprocess
import cohere
import requests
import json

app = Flask(__name__)

cohere_api_key = 'ArnEDE2bVtFU63oba6ErCIGAmqnQ7I5rAEByHYAF'
modelslab_api_key = "bELKhaucNeEMB7816sDiqWwuBeednfyRRQlwaUbSboq3jEkgspNDb57GLWbT"

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

@app.route('/generate_marketing', methods=['POST'])
def generate_marketing():
    data = request.json
    brand_name = data['brand_name']

    # Generate caption using Cohere
    co = cohere.Client(cohere_api_key)
    prompt = f"Generate a catchy marketing caption for the brand '{brand_name}'"
    cohere_response = co.generate(
        model='command-xlarge-nightly',
        prompt=prompt,
        max_tokens=50
    )
    generated_caption = cohere_response.generations[0].text

    # Generate image using Modelslab
    url = "https://modelslab.com/api/v6/realtime/text2img"
    payload = json.dumps({
        "key": modelslab_api_key,
        "prompt": f"Generate a catchy marketing picture for the brand {brand_name}",
        "negative_prompt": "bad quality",
        "width": "512",
        "height": "512",
        "safety_checker": False,
        "seed": None,
        "samples": 1,
        "base64": False,
        "webhook": None,
        "track_id": None
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {modelslab_api_key}'
    }
    response = requests.post(url, headers=headers, data=payload)
    response_data = response.json()

    if 'output' in response_data:
        image_url = response_data['output'][0]
    else:
        image_url = "Error: Image generation failed"

    return jsonify({
        "caption": generated_caption,
        "image_url": image_url
    })

if __name__ == '__main__':
    app.run(debug=True)