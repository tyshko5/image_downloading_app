import os

from flask import render_template, request, Blueprint, redirect, url_for
from werkzeug.utils import secure_filename

from app.controllers.from_json import from_json
from app.controllers.from_url import from_url
from app.controllers.save_file import save_file


main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'GET':
        return render_template(
            "index.html",
        )
    elif request.method == 'POST':
        uploaded_files = request.files.getlist("file[]")  # getting files
        for fi in uploaded_files:
            filename = secure_filename(fi.filename)
            if fi.mimetype.startswith("image"):  # in case of image
                save_file(filename, fi.read())
            elif fi.mimetype.endswith("json"):  # in case of json
                fi.save(os.path.join('./', filename))
                from_json(filename)
        if 'url[]' in request.form:
            url = request.form['url[]']
            if url != '':  # in case of url
                from_url(url)
        return redirect(
            url_for('main.index')
        )
