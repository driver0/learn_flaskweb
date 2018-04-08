#!/usr/bin/env python2
#-*- coding:utf-8 -*-

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Admin_cuiyihao <905073484@qq.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN','905073484@qq.com')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = os.environ.get('MAIL_SERVER','smtp.qq.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT','465'))
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL','True')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME','905073484@qq.com')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD','vrbhagxvwuohbbdc')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
            'sqlite:///'+os.path.join(basedir,'data-dev.sqlite')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
            'sqlite:///'+os.path.join(basedir,'data-test.sqlite')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
            'sqlite:///'+os.path.join(basedir,'data.sqlite')
config = {
        'development':DevelopmentConfig,
        'testing':TestingConfig,
        'production':ProductionConfig,
        
        'default':DevelopmentConfig
        }
