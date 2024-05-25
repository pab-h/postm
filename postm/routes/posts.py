from flask.blueprints import Blueprint

from postm.controllers.posts import PostsController
from postm.middlewares.authentication import AuthMiddleware

postsBp = Blueprint(
    name = "posts",
    import_name = __name__,
    url_prefix = "/posts" 
)

postsController = PostsController()

middleware = AuthMiddleware()

@postsBp.before_request
def postsMiddleware():
    return middleware.auth()

@postsBp.post("/create")
def createPost():
    return postsController.create()

@postsBp.get("/all")
def findAllPost():
    return postsController.findAll()

@postsBp.get("/find/<string:id>")
def findPostById(id: str):
    return postsController.findById(id)

@postsBp.delete("/delete/<string:id>")
def deletePost(id: str):
    return postsController.delete(id)

@postsBp.put("/update/<string:id>")
def updatePost(id: str):
    return postsController.update(id)

@postsBp.get("/all/page")
def findAllPostPaged():
    return postsController.findAllPaged()
