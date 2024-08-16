"""
    Módulo de configuração para pegar informações do .env
"""

from dotenv import load_dotenv
from .defaults import Constants, ENVNotFound
from os import environ

if not load_dotenv(Constants.ENVPATH):
    raise ENVNotFound("Environment file not found!")

# Add obligatory environment variables check (APP_PORT / API_KEY / ETC)
ENV = environ