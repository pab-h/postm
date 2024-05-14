from flask.blueprints import Blueprint
from postm.routes.posts import postsBp

apiBp = Blueprint(
    name = "api", 
    import_name = __name__, 
    url_prefix = "/api"
)

apiBp.register_blueprint(postsBp)
