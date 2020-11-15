import os

base_dir = os.path.dirname(os.path.abspath(__file__))


class BaseConfig(object):
    """Base configuration."""

    APP_NAME = 'Image Downloading App'
    DEBUG_TB_ENABLED = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Ensure you set a secret key, this is important!')
    UPLOAD_FOLDER = os.path.join(base_dir, 'upload')

    @staticmethod
    def configure(app):
        # Implement this method to do further configuration on your app.
        pass


class DevelopmentConfig(BaseConfig):
    """Development configuration."""

    DEBUG = True


class TestingConfig(BaseConfig):
    """Testing configuration."""

    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False


config = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=BaseConfig)
