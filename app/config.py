from os import environ


class Config(object):

    SECRET_KEY = 'my-secret-key'
    DEBUG = False

    #SQLALCHEMY_DATABASE_URI = "postgresql://postgre:giovanni@localhost/woodie"
    #SQLALCHEMY_DATABASE_URI = "sqlite:////Users/giovanni/PycharmProjects/web_application/app/woodie.db"
    SQLALCHEMY_DATABASE_URI = "sqlite:///site.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

