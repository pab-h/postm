from postm.entities.post import Post
from postm.database import database 
from uuid import uuid4 as uuid
from datetime import datetime

class PostRepository(object):

    def __init__(self) -> None:
        self.collection = database["posts"]

    def createPost(self, title: str, description: str, image: str = None) -> Post:
        post = Post(
            id = uuid(),
            title = title,
            description = description,
            image = image,
            created_at = datetime.now(),
            updated_at = datetime.now()
        )

        self.collection.insert_one(
            document = post.toJson()
        )
