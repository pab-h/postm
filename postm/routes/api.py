from flask.blueprints import Blueprint

from postm.routes.posts import postsBp
from postm.routes.users import usersBp

apiBp = Blueprint(
    name = "api", 
    import_name = __name__, 
    url_prefix = "/api"
)

apiBp.register_blueprint(postsBp)
apiBp.register_blueprint(usersBp)
