from dotenv import load_dotenv

if not load_dotenv(override=True):
    raise Exception("Unable to load settings file (.env)")

from flask import Flask
from postm.routes.api import apiBp

app = Flask(__name__)

app.register_blueprint(apiBp)
