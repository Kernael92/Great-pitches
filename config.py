import os


class Config:
    '''
    General configuration parent class
    '''
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

