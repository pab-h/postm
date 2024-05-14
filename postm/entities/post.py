from dataclasses import dataclass

from uuid import UUID

from datetime import datetime

@dataclass
class Post(object):
    id: UUID
    title: str
    image: str | None
    description: str
    created_at: datetime
    updated_at: datetime

    def toJson(self) -> dict[str, str]:
        return {
            "id": str(self.id),
            "title": str(self.title),
            "image": self.image,
            "description": self.description,
            "created_at": self.created_at.strftime("%d/%m/%Y %H:%M"),
            "updated_at": self.updated_at.strftime("%d/%m/%Y %H:%M"),
        }
