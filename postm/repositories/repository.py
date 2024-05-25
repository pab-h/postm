import os

from abc import ABC
from datetime import datetime
from uuid import uuid4 as uuid
from werkzeug.datastructures import FileStorage

class Repository(ABC):
    def __init__(self) -> None:
        super().__init__()

    def nowTime(self) -> str:
        return datetime.now().strftime("%d/%m/%Y %H:%M")

    def saveFileInDisk(self, file: FileStorage) -> str:
        extension = file.filename.split(".").pop()
        newFilename = f"{ uuid() }.{ extension }"
        
        uploadFolder = os.getenv("UPLOAD_FOLDER")

        if not os.path.exists(uploadFolder):
            os.makedirs(uploadFolder)

        filePath = os.path.join(
            uploadFolder,
            newFilename
        ) 

        file.save(filePath)

        return newFilename
