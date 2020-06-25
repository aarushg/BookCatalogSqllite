class BaseConfig(object):
    """Base configuration."""

    # main config
    SECRET_KEY = 'secret!'
    SQLALCHEMY_DATABASE_URI = 'sqlite:////Users/aarushg/Projects/WebDev/Flask/Book/database.db'
    SECURITY_PASSWORD_SALT = 'my_precious_two'
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    WTF_CSRF_ENABLED = True
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    # mail settings
    MAIL_SERVER = 'smtp.ionos.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    # MAIL_USE_SSL = False

    # gmail authentication
    MAIL_USERNAME = 'bookcatalog@aarushg.com'
    MAIL_PASSWORD = '@B00kcatalog'

    # mail accounts
    MAIL_DEFAULT_SENDER = 'bookcatalog@aarushg.com'
