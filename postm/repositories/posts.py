from postm.entities.post import Post
from postm.database import database 

from uuid import uuid4 as uuid

from datetime import datetime

class PostRepository(object):

    def __init__(self) -> None:
        self.collection = database["posts"]

    def create(self, title: str, description: str, image: str = None) -> Post:
        post = Post(
            id = str(uuid()),
            title = title,
            description = description,
            image = image,
            createdAt = datetime.now().strftime("%d/%m/%Y %H:%M"),
            updatedAt = datetime.now().strftime("%d/%m/%Y %H:%M")
        )

        self.collection.insert_one(
            document = post.toJson()
        )

        return post
    
    def findAll(self) -> list[Post]:
        postsDict: list[dict] = self.collection.find()

        posts = []

        for post in postsDict:
            post = Post(
                id = post.get("id", ""),
                title = post.get("title", ""),
                description = post.get("description", ""),
                image = post.get("image", ""),
                createdAt = post.get("createdAt", ""),
                updatedAt = post.get("updatedAt", "")
            )

            posts.append(post)

        return posts
    
    def findById(self, id: str) -> Post | None:
        post: dict = self.collection.find_one({
            "id": id
        })

        if not post:
            return None
        
        return Post(
            id = post.get("id", ""),
            title = post.get("title", ""),
            image = post.get("image", ""),
            description = post.get("description", ""),
            createdAt = post.get("createdAt", ""),
            updatedAt = post.get("updatedAt", "")
        )
    
    def delete(self, id: str) -> bool:
        result = self.collection.delete_one({
            "id": id
        })

        return result.deleted_count > 0