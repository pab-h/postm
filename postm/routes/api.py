from flask.blueprints import Blueprint
from flask import send_from_directory

from os import getenv

import os

from postm.routes.posts import postsBp
from postm.routes.users import usersBp
from postm.middlewares.authentication import AuthMiddleware

apiBp = Blueprint(
    name = "api", 
    import_name = __name__, 
    url_prefix = "/api"
)

apiBp.register_blueprint(postsBp)
apiBp.register_blueprint(usersBp)

middleware = AuthMiddleware()

@apiBp.get("/images/<string:name>")
def imageUploaded(name: str):
    authResponse = middleware.auth()

    if authResponse:
        return authResponse

    directoryPath = os.path.join(
        os.getcwd(), 
        getenv("UPLOAD_FOLDER")
    )

    return send_from_directory(
        directory = directoryPath,
        path = name
    )
