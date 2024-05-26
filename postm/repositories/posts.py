import os

from postm.entities.post import Post
from postm.database import database 
from postm.repositories.repository import Repository

from uuid import uuid4 as uuid
from dataclasses import dataclass
from werkzeug.datastructures import FileStorage

@dataclass
class PostPage(object):
    posts: list[Post]
    index: int
    size: int

class PostRepository(Repository):
    def __init__(self) -> None:
        super().__init__()

        self.collection = database.get_collection("posts")

    def create(self, title: str, description: str, image: FileStorage) -> Post:
        if image:
            image = self.saveFileInDisk(image)

        post = Post(
            id = str(uuid()),
            title = title,
            description = description,
            image = image,
            createdAt = self.nowTime(),
            updatedAt = self.nowTime()
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
    
    def findById(self, id: str) -> Post:
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
        post = self.findById(id)

        if post.image:
            os.remove(
                os.path.join(
                    os.getenv("UPLOAD_FOLDER"),
                    post.image
                )
            )

        result = self.collection.delete_one({
            "id": id
        })

        return result.deleted_count > 0
    
    def update(self, id: str, title: str, description: str, image: FileStorage) -> bool:
        oldPost = self.findById(id = id)

        newImage = oldPost.image

        if image:
            newImage = self.saveFileInDisk(image)
            os.remove(oldPost.image)

        updatedPost = Post(
            id = id,
            title = title,
            description = description,
            image = newImage,
            createdAt = oldPost.createdAt,
            updatedAt = self.nowTime()
        )

        result = self.collection.replace_one(
            filter = { "id": id },
            replacement = updatedPost.toJson()
        )

        return result.modified_count > 0

    def findAllPaged(self, index: int, size: int) -> PostPage:
        posts = []
        
        skip = size * index
        
        results = self.collection\
                .find()\
                .skip(skip)\
                .limit(size)
        
        for postDict in results:
            post = Post(
                id = postDict.get("id", ""),
                title = postDict.get("title", ""),
                image = postDict.get("image", ""),
                description = postDict.get("description", ""),
                createdAt = postDict.get("createdAt", ""),
                updatedAt = postDict.get("updatedAt", "")
            )

            posts.append(post)

        return PostPage(
            posts = posts,
            index = index,
            size = size
        )
    