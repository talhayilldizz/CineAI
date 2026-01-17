from app import create_app
from dotenv import load_dotenv
import os

# .env dosyasındaki şifreleri yükle
load_dotenv()

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)