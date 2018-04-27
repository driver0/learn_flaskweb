#!/usr/bin/env python2
#-*- coding:utf-8 -*-

from flask import Blueprint

api = Blueprint('api', __name__)

from . import authentication, posts, users, comments, errors
