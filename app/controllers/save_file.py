import os

from flask import current_app

from const import TESTING_DIR


# To simplify saving files in testing and deployment scenarios
def save_file(filename: str, data: bytes):
    if current_app:
        filename = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
    else:
        filename = os.path.join(TESTING_DIR, filename)
    with open(filename, mode='wb') as file:
        file.write(data)
