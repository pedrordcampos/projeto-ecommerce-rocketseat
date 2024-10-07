import os

class Config:
    # Configuração do Banco de Dados
    SQLALCHEMY_DATABASE_URI = 'sqlite:///ecommere.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
