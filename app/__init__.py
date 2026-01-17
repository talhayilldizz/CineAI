from flask import Flask
import os

def create_app():
    app = Flask(__name__)
    
    # Rota dosyasını (Blueprint) kaydet
    from app.routes import main
    app.register_blueprint(main)
    
    return app