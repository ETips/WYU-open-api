# -*- coding: utf-8 -*-

from flask import Blueprint

bp = Blueprint('account', __name__)


@bp.route('/')
def home():
    return 'account home page'


@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    return 'signup'


@bp.route('/login', methods=['GET', 'POST'])
def login():
    return 'login'