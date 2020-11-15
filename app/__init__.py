import os

from flask import Flask, render_template
from werkzeug.exceptions import HTTPException
from config import config


def create_app(environment='dev'):
    from app.views.main import main_blueprint
    # Instantiate app.
    app = Flask(__name__)

    # Set app config.
    env = os.environ.get('FLASK_ENV', environment)
    app.config.from_object(config[env])
    config[env].configure(app)

    app.register_blueprint(main_blueprint)

    # Error handlers.
    @app.errorhandler(HTTPException)
    def handle_http_error(error):
        return render_template('error.html', error=error), error.code

    return app
