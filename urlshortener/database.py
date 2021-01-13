import click
from flask_sqlalchemy import SQLAlchemy
from flask import current_app, g
from flask.cli import with_appcontext
import logging

db = SQLAlchemy()

logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.WARN)


def init_db():
    db.drop_all()
    db.create_all()


@click.command("init-db")
@with_appcontext
def init_db_command():
    init_db()
    click.echo("Initialized the database.")


def init_app(app):
    db.init_app(app)
    app.cli.add_command(init_db_command)
