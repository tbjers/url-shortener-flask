import os

from flask import Flask
from flask_cors import CORS

def create_app(config=None):
    """Creates and configures a Flask application

    :param config: Configuration mapping, primarily used for testing
    :returns: A Flask application"""

    app = Flask(__name__, instance_relative_config=True)

    if 'FLASK_SECRET_KEY' in os.environ:
        app.secret_key = os.environ['FLASK_SECRET_KEY']

    if 'SQLALCHEMY_DATABASE_URI' in os.environ:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']

    if 'SQLALCHEMY_TRACK_MODIFICATIONS' in os.environ:
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.environ['SQLALCHEMY_TRACK_MODIFICATIONS']

    if config:
        app.config.from_mapping(config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # set up CORS configuration
    CORS(app)

    # import dependencies
    from . import (
        database, shortener
    )

    # initialize the database connection
    database.init_app(app)

    # register application blueprints
    app.register_blueprint(shortener.bp)

    return app
