import cohere
import requests
import json

# Replace 'your_api_key' with your actual Cohere API key
cohere_api_key = 'ArnEDE2bVtFU63oba6ErCIGAmqnQ7I5rAEByHYAF'
co = cohere.Client(cohere_api_key)

# Example prompt for generating social media captions
brand_name = input("Enter your brand name and a detailed description of what you would like to be included in your marketing: ")
prompt = f"Generate a catchy marketing caption for the brand '{brand_name}'"

# Generate text using Cohere
cohere_response = co.generate(
    model='command-xlarge-nightly',  # Ensure this model ID is correct
    prompt=prompt,
    max_tokens=50  # Limit on how long the generated text should be
)

# Print the generated caption from Cohere
print("Generated Caption: ", cohere_response.generations[0].text)

# Your Modelslab Stable Diffusion API key
api_key = "bELKhaucNeEMB7816sDiqWwuBeednfyRRQlwaUbSboq3jEkgspNDb57GLWbT"

url = "https://modelslab.com/api/v6/realtime/text2img"

payload = json.dumps({
    "key": api_key,  # Add the API key here if required
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
    'Authorization': f'Bearer {api_key}'  # Add the Authorization header with the API key
}

response = requests.post(url, headers=headers, data=payload)

response_data = response.json()

# Extract and print the image URL from the response
if 'output' in response_data:
    image_url = response_data['output'][0]
    print("Image URL:", image_url)
else:
    print("Error: 'output' field not found in the response.")


