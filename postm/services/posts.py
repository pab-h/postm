from postm.repositories.posts import PostRepository
from postm.entities.post import Post

class PostCreateError(Exception):
    pass

class PostsService(object):
    def __init__(self) -> None:
        self.repository = PostRepository()

    def createPost(self, title: str, description: str, image: str = None) -> Post:
        if not title:
            raise PostCreateError("title is not provided")
        
        if not description:
            raise PostCreateError("description is not provided")
        
        return self.repository.createPost(
            title = title, 
            description = description, 
            image = image
        )
