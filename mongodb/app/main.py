from fastapi import FastAPI
from model import Person
from odmantic import AIOEngine
from motor.motor_asyncio import AsyncIOMotorClient


app = FastAPI()
client = AsyncIOMotorClient("mongodb://admin:admin@mongodb:27017/main?authSource=admin")
engine = AIOEngine(client=client)


instances = [
    Person(name="HarperCollins", age=12, email="harper@gmail.com"),
    Person(name="Hachette Livre", age=18, email="hachettelivre@gmail.com"),
    Person(name="Lulu", age=22)
]

@app.get("/")
def index():
    return {"You're in Index"}

@app.get("/persist_default_person/")
async def persist_to_db():
    try:
        print(await engine.save_all(instances))
    except Exception as e:
        print(e)
    return "Default 3 person were aded to the database"
