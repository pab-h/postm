from flask.blueprints import Blueprint

from postm.controllers.users import UsersController
from postm.middlewares.authentication import AuthMiddleware

middleware = AuthMiddleware()

usersBp = Blueprint(
    name = "users",
    import_name = __name__,
    url_prefix = "/users" 
)

usersController = UsersController()

@usersBp.post("/create")
def createUser():
    return usersController.create()

@usersBp.post("/login")
def loginUser():
    return usersController.login()

@usersBp.delete("/delete")
def deleteUser():
    authResponse = middleware.auth()

    if authResponse:
        return authResponse

    return usersController.delete()

@usersBp.put("/update")
def updateUser():
    authResponse = middleware.auth()

    if authResponse:
        return authResponse

    return usersController.update()
