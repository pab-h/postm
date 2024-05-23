from postm.database import database
from postm.entities.user import User
from postm.repositories.repository import Repository

from uuid import uuid4 as uuid

from hashlib import sha256

class UserRepository(Repository):

    def __init__(self) -> None:
        super().__init__()    
        self.collection = database.get_collection("users")
    
    def create(self, username: str, email: str, password: str) -> User:
        user = User(
            id = str(uuid()),
            username = username,
            email = email, 
            password = sha256(password.encode())\
                .hexdigest(),
            createdAt = self.nowTime(),
            updatedAt = self.nowTime(),   
        )

        self.collection.insert_one(
            document = user.toJson()
        )

        return user
    
    def findByEmail(self, email: str) -> User:
        user: dict = self.collection.find_one({ 
            "email": email 
        })

        if not user:
            return None

        return User(
            id = user.get("id", ""),
            username = user.get("username", ""),
            email = user.get("email", ""),
            password = user.get("password", ""),
            createdAt = user.get("createdAt", ""),
            updatedAt = user.get("updatedAt", "")
        )
    
    def findById(self, id: str) -> User:
        user: dict = self.collection.find_one({ 
            "id": id 
        })

        if not user:
            return None

        return User(
            id = user.get("id", ""),
            username = user.get("username", ""),
            email = user.get("email", ""),
            password = user.get("password", ""),
            createdAt = user.get("createdAt", ""),
            updatedAt = user.get("updatedAt", "")
        )
    
    def delete(self, id: str) -> bool:
        result = self.collection.delete_one({
            "id": id
        })

        return result.deleted_count > 0
    
    def update(self, id: str, username: str, email: str, password: str) -> User:
        userOld = self.findById(id)

        userUpdated = User(
            id = id,
            username = username,
            email = email,
            password = sha256(password.encode())\
                .hexdigest(),
            createdAt = userOld.createdAt,
            updatedAt = self.nowTime()
        )

        self.collection.replace_one(
            filter = { "id": id },
            replacement = userUpdated.toJson()
        )

        return userUpdated
        