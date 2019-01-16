import os
import unittest
import coverage

def run():
    os.environ['FLASK_CONFIG'] = 'testing'

    os.environ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    os.environ['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    cov = coverage.Coverage(branch=True)
    cov.start()

    tests = unittest.TestLoader().discover('.')
    ok = unittest.TextTestRunner(verbosity=2).run(tests).wasSuccessful()

    cov.stop()
    print('')
    cov.report(omit=['manage.py', 'tests/*'])
