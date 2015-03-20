# -*- coding: utf-8 -*-
from flask import Blueprint
from ..utils.common import response_json
from service.wyulibrary import WyuLibrary

bp = Blueprint('library', __name__)

@bp.route('/search/<string:keyword>')
@bp.route('/search/<string:keyword>/page/<int:page>')
def search_book(keyword='', page=1):
    lib = WyuLibrary()
    try:
        return response_json(lib.search_book(keyword.encode('utf-8'), page))
    except Exception as e:
        return response_json(e.__str__())


@bp.route('/book/<int:ctrlno>')
def book_status(ctrlno):
    lib = WyuLibrary()
    try:
        return response_json(lib.book_status(ctrlno))
    except Exception as e:
        return response_json(e.__str__())

