# -*- coding: utf-8 -*-
from flask import Blueprint, request
from ..utils.common import response_json
from service.wyunews import WyuNews

bp = Blueprint('news', __name__)


@bp.route('/list/<int:page>')
def news_list(page=1):
    page = 1 if page < 1 else page
    wyunews = WyuNews()
    try:
        return response_json(wyunews.get_wyu_news(page))
    except Exception as e:
        return response_json(e.message, 400)


@bp.route('/detail')
def news_detail():
    url = request.args['url']
    if url is None:
        return response_json('require params `url`')
    wyunews = WyuNews()
    try:
        return response_json({
            'contnet':wyunews.get_news_content(url)
        })
    except Exception as e:
        print e
        return response_json(e.message, 400)


