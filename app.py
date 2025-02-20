from dotenv import load_dotenv
from website import create_app
from flask import Flask
import os

load_dotenv()

HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
DEBUG = os.getenv("DEBUG")
SECRET_KEY = os.getenv("SECRET_KEY")

def main():
    app: Flask = create_app()
    app.secret_key = SECRET_KEY
    app.run(host=HOST, port=PORT, debug=DEBUG)

if __name__ == '__main__':
    main()
    