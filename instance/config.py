# config.py


class Config(object):
    """Parent configuration class."""
    DEBUG = False
    TESTING = False
    SECRET_KEY = "some-very-long-string-of-random-characters-CHANGE-TO-LIKING"
    ERROR_404_HELP = False


class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True
    # MODE="development"


class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    DEBUG = True
    # MODE="testing"


class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}
