from postm.repositories.users import UserRepository
from postm.entities.user import User

from os import getenv
from hashlib import sha256
from jwt import encode

from datetime import datetime
from datetime import timedelta

from datetime import timezone

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
        
        if self.findByEmail(email):
            raise Exception(f"email { email } already exists")
        
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
        
        exp = datetime.now(timezone.utc) + timedelta(
            seconds = float(getenv("JWT_DURATION", 3600))
        )

        return encode(
            payload = { 
                "id": user.id,
                "exp": exp
            },
            key = getenv("JWT_KEY"),
        )
    
    def findByEmail(self, email: str) -> User:
        return self.repository.findByEmail(
            email = email
        )
    
    def findById(self, id: str) -> User:
        return self.repository.findById(id)

    def delete(self, id: str) -> bool:
        if not id:
            raise Exception("id is not provided")

        return self.repository.delete(id)
    
    def update(self, id: str, username: str, email: str, password: str) -> User:
        if not id:
            raise Exception("id is not provided")
        
        if not username:
            raise Exception("username is not provided")
        
        if not email:
            raise Exception("email is not provided")
        
        if not password:
            raise Exception("password is not provided")
        
        if self.findByEmail(email):
            raise Exception(f"email { email } already exists")
        
        return self.repository.update(
            id = id,
            username = username,
            email = email,
            password = password
        )
    