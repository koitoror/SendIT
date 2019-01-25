# config.py
import os


class Config(object):
    """Parent configuration class."""
    DEBUG = False
    TESTING = False
    SECRET_KEY = "some-very-long-string-of-random-characters-CHANGE-TO-LIKING"
    ERROR_404_HELP = False
    
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv('GMAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('GMAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.getenv('Admin','GMAIL_MAIL')
    MAIL_SUPPRESS_SEND = True
    MAIL_ASCII_ATTACHMENTS = False

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
    DATABASE_URL = os.getenv("DATABASE_URL")


class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    DEBUG = True
    MODE = "testing"
    DATABASE_URL = os.getenv("TEST_DB_URL")


class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    DATABASE_URL = os.getenv("PROD_DB_URL")


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}
