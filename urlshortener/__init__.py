import os

from flask import Flask
from flask_cors import CORS
from flask_babel import Babel

def create_app(config=None):
    """Creates and configures a Flask application

    :param config: Configuration object, primarily used for testing
    :returns: A Flask application"""

    app = Flask(__name__, instance_relative_config=True)

    if 'FLASK_SECRET_KEY' in os.environ:
        app.secret_key = os.environ['FLASK_SECRET_KEY']

    if 'SQLALCHEMY_DATABASE_URI' in os.environ:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']

    if 'SQLALCHEMY_TRACK_MODIFICATIONS' in os.environ:
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.environ['SQLALCHEMY_TRACK_MODIFICATIONS']

    if 'BABEL_DEFAULT_LOCALE' in os.environ:
        app.config['BABEL_DEFAULT_LOCALE'] = os.environ['BABEL_DEFAULT_LOCALE']
    else:
        app.config['BABEL_DEFAULT_LOCALE'] = 'en'

    if config:
        app.config.from_object(config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # set up CORS configuration
    CORS(app)

    # Set up i18n/l10n support with Babel
    babel = Babel(app)

    # import dependencies
    from . import (
        about, database, filters, handlers, legal, shortener
    )

    # initialize handlers
    handlers.init_handlers(app)

    # initialize filters
    filters.init_filters(app)

    # initialize the database connection
    database.init_app(app)

    # register application blueprints
    app.register_blueprint(about.bp)
    app.register_blueprint(legal.bp)
    app.register_blueprint(shortener.bp)

    return app
