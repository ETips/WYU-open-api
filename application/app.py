from flask import Flask
from handlers import account, home, user


def create_app():
    app = Flask(__name__)

    app.register_blueprint(home.bp)
    app.register_blueprint(account.bp, url_prefix='/account')
    app.register_blueprint(user.bp, url_prefix='/user')

    return app

