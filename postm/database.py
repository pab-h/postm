import pymongo

from os import getenv

client = pymongo.MongoClient(
    host = getenv("DB_HOST", ""),
    port = int(getenv("DB_PORT", "")),
    username = getenv("DB_USER", ""),
    password = getenv("DB_PASSWORD", ""),
)

database = client.get_database(
    name = getenv("DB_NAME", "") 
)
