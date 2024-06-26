from flask import request

from postm.services.users import UsersService

class UsersController(object):
    def __init__(self) -> None:
        self.service = UsersService()

    def create(self) -> tuple[dict, int]:
        if not request.is_json:
            return {
                "error": "the body needs to be a json"
            }, 400


        data: dict = request.get_json()

        username: str = data.get("username", "")
        email: str = data.get("email", "")
        password: str = data.get("password", "")

        try:
            user = self.service.create(
                username = username, 
                email = email, 
                password = password
            )

            user.password = None

            return user.toJson(), 200

        except Exception as error:
            return {
                "error": str(error)
            }, 400

    def login(self) -> tuple[dict, int]:
        if not request.is_json:
            return {
                "error": "the body needs to be a json"
            }, 400


        data: dict = request.get_json()

        email: str = data.get("email", "")
        password: str = data.get("password", "")      

        try:
            token = self.service.login(
                email = email,
                password = password
            )

            return {
                "token": token
            }, 200

        except Exception as exception:
            (error, status) = exception.args

            return {
                "error": error
            }, status

    def delete(self) -> tuple[dict, int]:
        try:
            id = request.user.id

            if not self.service.delete(id): 
                return {
                    "message": f"Unable to remove user { id }"
                }, 400
            
            return {
                "message": f"user { id } removed"
            }, 200
    
        except Exception as error:
            return {
                "error": str(error)
            }, 400
        
    def update(self) -> tuple[dict, int]:
        if not request.is_json:
            return {
                "error": "the body needs to be a json"
            }, 400


        data: dict = request.get_json()

        id = request.user.id

        username: str = data.get("username", "")
        email: str = data.get("email", "")
        password: str = data.get("password", "")

        try:
            user = self.service.update(
                id = id,
                username = username, 
                email = email, 
                password = password
            )

            user.password = None

            return user.toJson(), 200

        except Exception as error:
            return {
                "error": str(error)
            }, 400
        