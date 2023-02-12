from flask import Flask

from config import Config
from book_app.extensions import db


def init_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    from book_app.views import books as bp
    app.register_blueprint(bp)

    return app
