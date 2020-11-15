import json
import base64

FILES_FOR_TESTING = '../files_for_testing/'
JSON_TESTING_DIR = FILES_FOR_TESTING + 'json/'
IMAGES_TESTING_DIR = FILES_FOR_TESTING + 'images/'


def img_to_json(filename):
    data = {}
    json_filename = filename.split('.')[-2] + '.json'  # name with which the file will be saved at 'tests/files_for_testing/json' directory
    filename = IMAGES_TESTING_DIR + filename
    with open(filename, mode='rb') as file:
        img = file.read()
    data['img'] = base64.b64encode(img).decode("utf-8")  # encoding to base64
    json_filename = JSON_TESTING_DIR + json_filename
    with open(json_filename, mode='w') as file:
        file.write(json.dumps(data))
