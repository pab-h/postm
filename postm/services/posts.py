from postm.repositories.posts import PostRepository
from postm.entities.post import Post

class PostCreateError(Exception):
    pass

class PostFindError(Exception):
    pass

class PostDeleteError(Exception):
    pass

class PostsService(object):
    def __init__(self) -> None:
        self.repository = PostRepository()

    def create(self, title: str, description: str, image: str = None) -> Post:
        if not title:
            raise PostCreateError("title is not provided")
        
        if not description:
            raise PostCreateError("description is not provided")
        
        return self.repository.create(
            title = title, 
            description = description, 
            image = image
        )

    def findAll(self) -> list[Post]:
        return self.repository.findAll()

    def findById(self, id: str) -> Post | None:
        post = self.repository.findById(id)

        if not post:
            raise PostFindError(f"post { id } not exists")

        return post
    
    def delete(self, id: str) -> bool:
        post = self.findById(id)

        if not post:
            raise PostDeleteError(f"post { id } not exists")

        return self.repository.delete(id)
    