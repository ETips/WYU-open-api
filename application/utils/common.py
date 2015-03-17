# -*- coding: utf-8 -*-
from flask import make_response
import json


def response_json(json_obj, status_code=200, headers=None):
    """
    封装一个返回json字符串的响应
    :param json_obj: json object
    :param status_code: 状态码，默认200
    :param headers: 响应头
    :return: response
    """
    if isinstance(json_obj, str) or isinstance(json_obj, unicode):
        json_obj = {
            'msg' : json_obj
        }
    return make_response(json.dumps(json_obj), status_code, headers)