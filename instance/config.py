# config.py


class Config(object):
    """Parent configuration class."""
    DEBUG = False
    TESTING = False
    SECRET_KEY = "some-very-long-string-of-random-characters-CHANGE-TO-LIKING"
    ERROR_404_HELP = False
    # MAIL_SERVER = default ‘localhost’
    # MAIL_PORT = default 25
    # MAIL_USE_TLS = default False
    # MAIL_USE_SSL = default False
    # MAIL_DEBUG = default app.debug
    # MAIL_USERNAME = default None
    # MAIL_PASSWORD = default None
    # MAIL_DEFAULT_SENDER = default None
    # MAIL_MAX_EMAILS = default None
    # MAIL_SUPPRESS_SEND = default app.testing
    # MAIL_ASCII_ATTACHMENTS = default False


class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True
    MODE = "development"


class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    DEBUG = True
    MODE = "testing"


class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}
