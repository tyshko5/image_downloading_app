import os
import io

import pytest


from werkzeug.datastructures import FileStorage

from app import create_app

from const import DEPLOY_DIR, IMAGES_TESTING_DIR


@pytest.fixture
def client():
    app = create_app(environment="test")
    app.config["TESTING"] = True

    with app.test_client() as client:
        app_ctx = app.app_context()
        app_ctx.push()
        yield client
        app_ctx.pop()


def test_single_image(client):
    filename = 'lion.jpg'
    path = os.path.join(IMAGES_TESTING_DIR, filename)
    with open(path, "rb") as f:
        data = f.read()
    file_to_test = FileStorage(  # simulating download process
        stream=io.BytesIO(data),
        filename=filename,  # name with which the file will be saved at ./upload directory
        content_type="image/jpg",
    )
    data = {'file[]': file_to_test}  # prepared data to be sent
    response = client.post('/', data=data, content_type="multipart/form-data")
    assert response.status_code == 302
    path_filename = os.path.join(DEPLOY_DIR, filename)
    assert os.path.exists(path_filename)  # checking if the file was actually downloaded


def test_multiple_images(client):
    filenames = ['lion.jpg', 'oak-tree-pic.jpg']
    paths = [os.path.join(IMAGES_TESTING_DIR, filename) for filename in filenames]
    files_to_test = []
    for path in paths:
        with open(path, "rb") as f:
            data = f.read()
        file_to_test = FileStorage(  # simulating download process
            stream=io.BytesIO(data),
            filename=path.split('/')[-1],  # name with which the file will be saved at ./upload directory
            content_type="image/jpg",
        )
        files_to_test.append(file_to_test)
    data = {'file[]': files_to_test}  # prepared data to be sent
    response = client.post('/', data=data, content_type="multipart/form-data")
    assert response.status_code == 302
    paths_filenames = [os.path.join(DEPLOY_DIR, filename) for filename in filenames]
    for path_filename in paths_filenames:
        assert os.path.exists(path_filename)  # checking if each file was actually downloaded
