import os
basedir = os.path.abspath(os.path.dirname(__file__))

import os
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = 1
    MAIL_USERNAME = 'alfatihridho@gmail.com'
    MAIL_PASSWORD = 'vhitrohqvjtntzmg'
    ADMINS = ['doalfatih@gmail.com']
    POSTS_PER_PAGE = 3
    LANGUAGES = ['en', 'in']
    MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')