#DALLE
from io import BytesIO

import requests

from utils.util import save_image_by_url

secret=""

import os
import openai

#Mettre votre token
openai.api_key="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"


def get_all_model():
    return openai.Model.list()

def create_image_by_prompt(prompt:str):
    """
    Une fonction qui va prendre en entrée un prompt et va sortir l'url de l'image
    :param prompt:
    :return:
    """
    response=openai.Image.create(
        prompt=prompt,
        n=1,
        size='256x256'
    )
    return response['data'][0]['url']

def create_variation_image(image_url):
    response = requests.get(image_url)
    image = response.content

    response = openai.Image.create_variation(
        image=BytesIO(image),
        n=1,
        size="1024x1024"
    )
    return response['data'][0]['url']