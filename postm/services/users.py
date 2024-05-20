from postm.repositories.users import UserRepository

from postm.entities.user import User

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
