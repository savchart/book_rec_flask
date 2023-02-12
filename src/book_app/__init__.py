from flask import Flask

from config import Config


def init_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from book_app.views import books as bp
    app.register_blueprint(bp)

    return app
