import os
import base64
import json

from flask import current_app

from app.controllers.save_file import save_file


def from_json(filename):
    with open(filename, "rb") as f:
        data = json.load(f)
        dict_keys = list(data.keys())
        key = dict_keys[0]  # taking data from first key
        image = base64.decodebytes(data[key].encode('utf-8'))  # decoding from base64
        new_filename = filename.split('/')[-1].split('.')[-2] + ".png"  # name with which the file will be saved at ./upload directory
        save_file(new_filename, image)
    if current_app:
        os.remove(filename)
