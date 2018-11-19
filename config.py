import os


class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kernaeljoy:benter92@localhost/pitches'
    SECRET_KEY='Powerfull SecretKey'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    #email configurations
    MAIL_SERVER = 'smtp.googleemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    pass
class ProdConfig(Config):
    '''
    Production configuration child class

    args:
        Config: The parent configuration class with the General configuration settings
        
    '''
    pass 
class DevConfig(Config):
    '''
    Development configuration child class

    args:
        Config: The parent configuration class with the General configuration settings 
    '''

    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}

