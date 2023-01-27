import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my_secret_key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True

    
    
#SECRET_KEY: Es una clave secreta utilizada para proteger la aplicación. Se establece utilizando una variable de entorno llamada 'SECRET_KEY', o utilizando un valor predeterminado 'my_secret_key' si no se encuentra la variable de entorno.
#SQLALCHEMY_DATABASE_URI: Es la URI de la base de datos que se utilizará para almacenar los datos de la aplicación. Se establece utilizando una variable de entorno llamada 'DATABASE_URL', o utilizando un valor predeterminado 'sqlite:///app.db' si no se encuentra la variable de entorno.
#SQLALCHEMY_TRACK_MODIFICATIONS: Establece si SQLAlchemy debe hacer un seguimiento de los cambios en las entidades. Se establece en False para mejorar el rendimiento.
#DEBUG: Establece si la aplicación se ejecuta en modo debug. Se establece en True para facilitar el desarrollo.
