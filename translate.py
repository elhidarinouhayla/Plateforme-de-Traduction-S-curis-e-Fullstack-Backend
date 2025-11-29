import os
from config import HF_TOKEN
import requests

# print(HF_TOKEN)
def translate(input_text, language):
    API_URL = f"https://router.huggingface.co/hf-inference/models/Helsinki-NLP/opus-mt-{language}"
    headers = {
        "Authorization": f"Bearer {HF_TOKEN}",
    }

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()

    output = query({
        "inputs": input_text,
    })
    return output
# print( translate("Hello Hassan", "en-fr"))