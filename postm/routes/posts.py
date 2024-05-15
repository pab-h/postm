from flask.blueprints import Blueprint
from postm.controllers.posts import PostsController

postsBp = Blueprint(
    name = "posts",
    import_name = __name__,
    url_prefix = "/posts" 
)

postsController = PostsController()

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
