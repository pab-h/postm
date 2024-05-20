from flask.blueprints import Blueprint
from postm.controllers.users import UsersController

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
