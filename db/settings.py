import os
from os.path import join, dirname
from dotenv import load_dotenv

from flask import Flask


dotenv_path = join(dirname(__name__), ".env")
load_dotenv(dotenv_path)
SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

print(SQLALCHEMY_DATABASE_URI)