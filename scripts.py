from postm.app import app

from os import getenv

def start() -> None:
    app.run(
        host = getenv("HOST", "localhost"),
        port= getenv("PORT", 5000)
    )
