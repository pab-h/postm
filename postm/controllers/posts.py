from flask import request

from postm.services.posts import PostsService
from postm.services.posts import PostCreateError

class PostsController(object):
    def __init__(self) -> None:
        self.service = PostsService()

    def createPost(self) -> tuple[dict, int]:
        if not request.is_json:
            return {
                "error": "the body needs to be json"
            }, 400

        data: dict = request.get_json()

        title: str = data.get("title", "")
        description: str = data.get("description", "")

        try:
            post = self.service.createPost(
                title = title,
                description = description,
                image = None
            )

            return post.toJson(), 200

        except PostCreateError as error:
            return {
                "error": str(error)
            }, 400
        
        except: 
            return {
                "error": "Something unexpected happened"
            }, 500