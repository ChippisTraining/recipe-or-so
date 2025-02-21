from dotenv import load_dotenv
from website import create_app
from flask import Flask
import os

load_dotenv()

HOST = os.getenv("HOST", "127.0.0.1")
PORT = os.getenv("PORT", 5000)
DEBUG = os.getenv("DEBUG", "false").lower() == "true"

def main():
    app: Flask = create_app()
    app.run(host=HOST, port=PORT, debug=DEBUG)

if __name__ == '__main__':
    main()
    