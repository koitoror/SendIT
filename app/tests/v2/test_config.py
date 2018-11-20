import unittest

# third-party imports
from flask_testing import TestCase

from run import app


class TestDevelopmentSettings(TestCase):
    """class for testing the development configs."""

    @classmethod
    def create_app(cls):
        app.config.from_object('instance.config.DevelopmentConfig')
        return app

    def test_development_config(self):
        self.assertFalse(app.config['SECRET_KEY'] is 'thisisit')
        self.assertFalse(app.config['DEBUG'] is False)



class TestTestingSettings(TestCase):
    """class for testing the testing configs."""

    @classmethod
    def create_app(cls):
        app.config.from_object('instance.config.TestingConfig')
        return app

    def test_testing_config(self):
        self.assertTrue(app.config['DEBUG'])
        self.assertTrue(app.config['TESTING'])


class TestProductionSettings(TestCase):
    """class for testing the production configs."""

    @classmethod
    def create_app(cls):
        app.config.from_object('instance.config.ProductionConfig')
        return app

    def test_production_configs(self):
        self.assertTrue(app.config['TESTING'] is False)


if __name__ == '__main__':
    unittest.main()