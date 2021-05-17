# -*- coding: utf-8 -*-
import os

class Config(object):
    SQLALCHEMY_DATABASE_URI = ''


class LocalConfig(Config):
    AMBIENTE = 'Local'
    DEBUG = True
    PORT = 5000
    CACHE_TYPE = "FileSystemCache",  # Flask-Caching related configs
    CACHE_DEFAULT_TIMEOUT = 30 * 24 * 60 * 60
    BASE_URL = 'http://127.0.0.1:5000'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SECURITY_PASSWORD_SALT = 'none'
    SECURITY_POST_LOGIN_VIEW = '/admin/'
    SECURITY_POST_LOGOUT_VIEW = '/admin/'
    SECURITY_POST_REGISTER_VIEW = '/admin/'
    SECURITY_POST_REGISTER_VIEW = '/admin/'
    SECURITY_REGISTERABLE = True
    SECURITY_SEND_REGISTER_EMAIL = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_ADMIN_SWATCH = 'cosmo'
    FLASK_ADMIN_FLUID_LAYOUT = True


