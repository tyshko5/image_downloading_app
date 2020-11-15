import os

from app.controllers.from_url import from_url
from const import TESTING_DIR


def test_image_from_url():
    url = 'https://cdn.mos.cms.futurecdn.net/9budkUADwqBCTvj4pCWcQi-320-80.jpg'
    filename = url.split('/')[-1]  # name with which the file will be saved at ./upload directory
    filename = os.path.join(TESTING_DIR, filename)
    from_url(url)
    assert os.path.exists(filename)  # checking if the file was actually downloaded
