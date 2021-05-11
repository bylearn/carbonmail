# Onde estarão todas as funções deste pacote.
# Ele é quem vai coordenar este pacote (gerenciador)

import urllib
import json
import os

import requests

from carbonmail.utils import root_folder


def extract_code(code_path):
    with open(code_path, encoding="utf-8") as code_file:
        code = code_file.read()

    code_encoded = urllib.parse.quote(code)

    return code_encoded


def prepare_payload(code_path):
    json_path = os.path.join(root_folder(), "config.json")

    with open(json_path) as json_file:
        payload = json.load(json_file)


    payload["code"] = extract_code(code_path)

    return payload


def download_image(code_path):
    # Não coloquem Localhost, coloquem o link de vocês
    api_url = "http://localhost:8000/api/cook"
    payload = prepare_payload(code_path)

    image_folder = os.path.join(root_folder(), "images")

    if not os.path.exists(image_folder):
        os.makedirs(image_folder)

    image_name = os.path.basename(code_path)  # D:\carbonmail\codes\teste.py
    image_name = os.path.splitext(image_name)[0]  # teste.py
    image_path = os.path.join(image_folder, f"{image_name}.png")  # teste

    response = requests.post(api_url, json=payload)

    with open(image_path, "wb") as image:
        image.write(response.content)

    return image_path
