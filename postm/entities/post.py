from dataclasses import dataclass

@dataclass
class Post(object):
    id: str
    title: str
    image: str | None
    description: str
    createdAt: str
    updatedAt: str

    def toJson(self) -> dict[str, str]:
        return {
            "id": self.id,
            "title": self.title,
            "image": self.image,
            "description": self.description,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt
        }
