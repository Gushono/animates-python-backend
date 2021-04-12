import os

SECRET_KEY = os.getenv("SECRET_KEY") or 'abracadabra'
DATABASE_URL = os.getenv("DATABASE_URL")
HOST = os.getenv("HOST") or "127.0.0.1"
