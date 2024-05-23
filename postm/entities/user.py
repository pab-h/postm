from dataclasses import dataclass

@dataclass
class User(object):
    id: str
    username: str
    email: str
    password: str        
    createdAt: str
    updatedAt: str

    def toJson(self) -> dict:
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt
        }
    