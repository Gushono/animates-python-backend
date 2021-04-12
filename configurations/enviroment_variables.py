import os

SECRET_KEY = os.getenv("SECRET_KEY") or 'abracadabra'
DATABASE_URL = os.getenv("DATABASE_URL")
