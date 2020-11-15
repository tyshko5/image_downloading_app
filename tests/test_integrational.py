import os
import io

import pytest

from werkzeug.datastructures import FileStorage

from app import create_app
from const import DEPLOY_DIR, JSON_TESTING_DIR


@pytest.fixture
def client():
    app = create_app(environment="test")
    app.config["TESTING"] = True

    with app.test_client() as client:
        app_ctx = app.app_context()
        app_ctx.push()
        yield client
        app_ctx.pop()


def test_integrational_json(client):
    filename = 'lion.json'
    path = os.path.join(JSON_TESTING_DIR, filename)
    with open(path, "rb") as f:
        data = f.read()
    file_to_test = FileStorage(  # simulating download process
        stream=io.BytesIO(data),
        filename=filename,  # name with which the file will be saved at ./upload directory
        content_type="application/json",
    )
    data = {'file[]': file_to_test}  # prepared data to be sent
    response = client.post('/', data=data, content_type="multipart/form-data")
    assert response.status_code == 302
    image_filename = filename.split('/')[-1].split('.')[-2] + '.png'  # name with which the file was presumably saved at ./upload directory
    image_filename = os.path.join(DEPLOY_DIR, image_filename)
    assert os.path.exists(image_filename)  # checking if the file was actually downloaded


def test_integrational_url(client):
    url = 'https://cdn.mos.cms.futurecdn.net/9budkUADwqBCTvj4pCWcQi-320-80.jpg'
    data = {'url[]': url}  # prepared data to be sent
    response = client.post('/', data=data)
    assert response.status_code == 302
    filename = url.split('/')[-1]  # name with which the file will be saved at ./upload directory
    filename = os.path.join(DEPLOY_DIR, filename)
    assert os.path.exists(filename)  # checking if the file was actually downloaded
