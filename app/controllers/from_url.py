import urllib.request

from app.controllers.save_file import save_file


# download and save image from url
def from_url(url: str):
    filename = url.split('/')[-1]  # name with which the file will be saved at ./upload directory
    with urllib.request.urlopen(url) as f:
        data = f.read()
        save_file(filename, data)
