from postm.repositories.posts import PostRepository
from postm.repositories.posts import PostPage

from postm.entities.post import Post

from werkzeug.datastructures import FileStorage

class PostsService(object):
    def __init__(self) -> None:
        self.repository = PostRepository()
        self.extensionsAllowed = ["png", "jpeg", "jpg", "gif"]

    def create(self, title: str, description: str, image: FileStorage) -> Post:
        if not title:
            raise Exception("title is not provided")
        
        if not description:
            raise Exception("description is not provided")
        
        if image:
            extension = image.filename\
                .split(".")\
                .pop()
            
            if extension not in self.extensionsAllowed:
                raise Exception(f"{ extension } not allowed")

        return self.repository.create(
            title = title, 
            description = description, 
            image = image
        )

    def findAll(self) -> list[Post]:
        return self.repository.findAll()

    def findById(self, id: str) -> Post:
        post = self.repository.findById(id)

        if not post:
            raise Exception(f"post { id } not exists")

        return post
    
    def delete(self, id: str) -> bool:
        post = self.repository.findById(id)

        if not post:
            raise Exception(f"post { id } not exists")

        return self.repository.delete(id)
    
    def update(self, id: str, title: str, description: str, image: FileStorage) -> bool:
        if not self.repository.findById(id):
            raise Exception(f"post { id } not exists")

        if not title:
            raise Exception("title is not provided")
        
        if not description:
            raise Exception("description is not provided")
        
        if image:
            extension = image.filename\
                .split(".")\
                .pop()
            
            if extension not in self.extensionsAllowed:
                raise Exception(f"{ extension } not allowed")

        return self.repository.update(
            id = id,
            title = title,
            description = description,
            image = image
        )
    
    def findAllPaged(self, index: int, size: int) -> PostPage:
        if not size > 0:
            raise Exception("size must be greater than zero")
        
        if not index >= 0:
            raise Exception("the index must be positive")

        return self.repository.findAllPaged(index, size)
