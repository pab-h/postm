import subprocess
from postm.app import app
from os import getenv

def start() -> None:
    app.run(
        host = getenv("HOST", "localhost"),
        port= getenv("PORT", 5000)
    )

def test() -> None:
    subprocess.run([
        "poetry", 
        "run", 
        "python", 
        "-m", 
        "unittest", 
        "discover"
    ])
