# app/__init__.py
import os
from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import Config

db = SQLAlchemy()

def create_app():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    frontend_dir = os.path.join(os.path.dirname(os.path.dirname(current_dir)), 'FRONTEND')

    app = Flask(__name__, static_folder=frontend_dir, static_url_path='')
    app.config.from_object(Config)

    instance_path = os.path.join(current_dir, 'instance')
    if not os.path.exists(instance_path):
        os.makedirs(instance_path)

    db.init_app(app)
    CORS(app)

    from .routes import api
    app.register_blueprint(api, url_prefix='/api')

    @app.route('/')
    def serve_index():
        return send_from_directory(app.static_folder, 'index.html')

    with app.app_context():
        db.create_all() 

    return app