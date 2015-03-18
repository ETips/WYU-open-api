# -*- coding: utf-8 -*-
from flask import Blueprint, request
from service.subsystem import SubSystem
from ..utils.common import response_json
bp = Blueprint('user', __name__)


@bp.route('/timetable', methods=['GET', 'POST'])
def get_timetalbe():
    if request.method == 'GET':
        return 'The timetable api'

    userid = request.form['userid']
    psw = request.form['psw']
    user = SubSystem(userid=userid, userpsw=psw)

    if user.login():
        return response_json(user.get_course())
    else:
        return response_json('登陆失败，请检查账号密码', 400)


@bp.route('/score', methods=['GET', 'POST'])
def get_score():
    if request.method == 'GET':
        return 'The score api'

    userid = request.form['userid']
    psw = request.form['psw']
    user = SubSystem(userid=userid, userpsw=psw)

    if user.login():
        return response_json(user.get_score())
    else:
        return response_json('登陆失败，请检查账号密码', 400)

