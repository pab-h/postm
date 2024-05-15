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
