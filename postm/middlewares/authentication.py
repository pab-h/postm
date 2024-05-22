from flask import request
from os import getenv

from jwt import decode
from jwt import ExpiredSignatureError

from postm.services.users import UsersService

class AuthMiddleware(object):

    def __init__(self) -> None:
        self.service = UsersService()

    def auth(self) -> None:
        authorization = request.headers.get("Authorization")

        if not authorization:
            return {
                "error": "an authentication token is required"
            }, 400
        
        parts = authorization.split(" ")

        if len(parts) != 2 or parts[0] != "Bearer":
            return {
                "error": "authentication token needs to be a jwt"
            }, 400
        
        tokenEncoded = parts[1]

        try:
            payload: dict = decode(
                jwt = tokenEncoded,
                key = getenv("JWT_KEY"),
                algorithms = ["HS256"]
            )

            email = payload.get("email", "")

            if not self.service.findByEmail(email):
                return {
                    "error": f"user { email } not found"
                }, 401
            
        except ExpiredSignatureError as error:
            return {
                "error": "token expired"
            }, 401  

        except Exception as error:
            return {
                "error": str(error)
            }, 500
