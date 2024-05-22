from postm.repositories.users import UserRepository
from postm.entities.user import User

from os import getenv
from hashlib import sha256
from jwt import encode
from time import time

class UsersService(object):
    def __init__(self) -> None:
        self.repository = UserRepository()

    def create(self, username: str, email: str, password: str) -> User:
        if not username:
            raise Exception("username is not provided")
        
        if not email:
            raise Exception("email is not provided")
        
        if not password:
            raise Exception("password is not provided")
        
        return self.repository.create(
            username = username, 
            email = email, 
            password = password
        )

    def login(self, email: str, password: str) -> str:
        if not email:
            raise Exception(
                "email is not provided",
                400 
            )
        
        if not password:
            raise Exception(
                "password is not provided",
                400
            )

        user = self.repository.findByEmail(
            email = email
        )

        if not user: 
            raise Exception(
                f"user { email } not exists",
                403    
            )
        
        passwordHash = sha256(password.encode())\
                        .hexdigest()

        if not user.password == passwordHash:
            raise Exception(
                f"wrong password for { email }",
                403    
            )

        return encode(
            payload = { "email": email },
            key = getenv("JWT_KEY"),
            headers = {
                "exp": time() + int(getenv("JWT_DURATION", 3600))
            }
        )
    
    def findByEmail(self, email: str) -> User:
        return self.repository.findByEmail(
            email = email
        )

    def delete(self, id: str) -> bool:
        if not id:
            raise Exception("id is not provided")

        return self.repository.delete(id)