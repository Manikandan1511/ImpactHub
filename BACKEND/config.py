# config.py
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-prod'
    
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app', 'instance', 'impactforge.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Blockchain Config
    WEB3_PROVIDER_URI = "http://127.0.0.1:8545" 
    CONTRACT_ADDRESS = "0xd9145CCE52D386f254917e481eB44e9943F39138"