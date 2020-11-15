import os

from app.controllers.from_json import from_json
from const import TESTING_DIR, JSON_TESTING_DIR


def test_image_from_json():
    filename = 'lion.json'
    image_filename = filename.split('/')[-1].split('.')[-2] + '.png'  # name with which the file will be saved at ./upload directory
    image_filename = os.path.join(TESTING_DIR, image_filename)
    path = os.path.join(JSON_TESTING_DIR, filename)
    from_json(path)
    assert os.path.exists(image_filename)  # checking if the file was actually downloaded
