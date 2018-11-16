import unittest

# third-party imports
from flask_testing import TestCase

# local imports
from run import app

class TestDevelopmentConfig(TestCase):
    """TestCase for the development config."""

    @classmethod
    def create_app(cls):
        app.config.from_object('instance.config.DevelopmentConfig')
        return app

    def test_development_configs(self):
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(app.config['SECRET_KEY'] is "thisismysecretkey")

class TestTestingConfig(TestCase):
    """TestCase for the testing config."""

    @classmethod
    def create_app(cls):
        app.config.from_object('instance.config.TestingConfig')
        return app

    def test_testing_configs(self):
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertTrue(app.config['TESTING'] is True)

class TestProductionConfig(TestCase):
    """TestCase for the development config."""

    @classmethod
    def create_app(cls):
        app.config.from_object('instance.config.ProductionConfig')
        return app

    def test_production_configs(self):
        self.assertFalse(app.config['DEBUG'] is True)
        self.assertFalse(app.config['TESTING'] is True)



if __name__ == "__main__":
    unittest.main()