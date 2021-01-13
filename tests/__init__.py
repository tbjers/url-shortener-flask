import os


def run():
    os.environ["FLASK_CONFIG"] = "testing"

    os.environ["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    os.environ["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
