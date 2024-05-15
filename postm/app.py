from flask import Flask

from postm.routes.api import apiBp

app = Flask(__name__)

app.register_blueprint(apiBp)
