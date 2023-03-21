import shutil
from pathlib import Path

import requests
import urllib.request


def save_image_by_url(url,path="default.jpg"):
    urllib.request.urlretrieve(url,
                               path)
    print("image save")
    return path


