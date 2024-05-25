from flask import request

from postm.services.posts import PostsService
from postm.repositories.posts import PostPage

from os import getenv

class PostsController(object):
    def __init__(self) -> None:
        self.service = PostsService()

    def create(self) -> tuple[dict, int]:

        data = request.form

        title: str = data.get("title", "")
        description: str = data.get("description", "")
        image = request.files.get("image", None)

        try:

            post = self.service.create(
                title = title,
                description = description,
                image = image
            )

            if post.image:
                post.image = f"{ getenv("URL") }/api/images/{ post.image }"

            return post.toJson(), 200

        except Exception as error:
            return {
                "error": str(error)
            }, 400
        
    def findAll(self) -> tuple[dict, int]:
        try: 
            posts = self.service.findAll()

            postsFormated = [post.toJson() for post in posts]

            return { "posts": postsFormated }, 200
        
        except: 
            return {
                "error": "Something unexpected happened"
            }, 500
    
    def findById(self, id: str) -> tuple[dict, int]:
        try:
            post = self.service.findById(id)

            return post.toJson(), 200
        
        except Exception as error:
            return {
                "error": str(error)
            }, 400

    def delete(self, id: str) -> tuple[dict, int]:
        try:
            if not self.service.delete(id): 
                return {
                    "message": f"Unable to remove post { id }"
                }, 400
            
            return {
                "message": f"post { id } removed"
            }, 200
    
        except Exception as error:
            return {
                "error": str(error)
            }, 400

    def update(self, id: str) -> tuple[dict, int]:

        data = request.form

        title: str = data.get("title", "")
        description: str = data.get("description", "")
        image = request.files.get("image", None)

        try:
            isUpdate = self.service.update(
                id = id,
                title = title,
                description = description,
                image = image
            )

            if not isUpdate: 
                return {
                    "message": f"Unable to update post { id }"
                }, 400
            
            return {
                "message": f"post { id } updated"
            }, 200

        except Exception as error:
            return {
                "error": str(error)
            }, 400
        
    def createNextUrlPage(self, page: PostPage) -> str:
        query = f"index={ page.index + 1 }&size={ page.size }"

        return f"{ getenv("URL") }/api/posts/all/page?{ query }"
    
    def createPreviousUrlPage(self, page: PostPage) -> str:
        if page.index - 1 < 0:
            return None 

        query = f"index={ page.index - 1 }&size={ page.size }"

        return f"{ getenv("URL") }/api/posts/all/page?{ query }"
        
    def findAllPaged(self) -> tuple[dict, int]:
        index = request.args.get("index", 0)
        size = request.args.get("size", 10)

        try: 
            index = int(index)
            size = int(size)

            postPage = self.service.findAllPaged(
                index = int(index),
                size = int(size)
            )

            postFormated = [ p.toJson() for p in postPage.posts ]

            nextUrl = self.createNextUrlPage(
                page = postPage
            )

            if not postFormated:
                nextUrl = None

            previousUrl = self.createPreviousUrlPage(
                page = postPage
            )

            return {
                "posts": postFormated,
                "next": nextUrl,
                "previous": previousUrl
            }, 200
        
        except Exception as error:
            return {
                "error": str(error)
            }, 400
        