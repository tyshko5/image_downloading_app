import os

base_dir = os.path.dirname(os.path.abspath(__file__))

TESTS_DIR = os.path.join(base_dir, 'tests/')
TESTING_DIR = os.path.join(TESTS_DIR, 'upload/')

FILES_FOR_TESTING = os.path.join(TESTS_DIR, 'files_for_testing/')
JSON_TESTING_DIR = os.path.join(FILES_FOR_TESTING, 'json/')
IMAGES_TESTING_DIR = os.path.join(FILES_FOR_TESTING, 'images/')

DEPLOY_DIR = os.path.join(base_dir, 'upload/')
