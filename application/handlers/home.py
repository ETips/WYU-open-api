# -*- coding: utf-8 -*-

from flask import Blueprint

bp = Blueprint('', __name__)


@bp.route('/')
def home():
    return 'Welcome to ETips open api!'



