import os
from config import HF_TOKEN
import requests


def translate(input_text, language):
    API_URL = "https://router.huggingface.co/hf-inference/models/Helsinki-NLP/opus-mt-fr-en"
    headers = {
        "Authorization": f"Bearer {os.environ['HF_TOKEN']}",
    }

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()

    output = query({
        "inputs": input_text,
    })
    return output