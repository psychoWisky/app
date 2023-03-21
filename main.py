
import json
from fastapi import FastAPI , Path
import requests


testAPI = FastAPI()

@testAPI.get("/")

async def req(id: str , gt=0, lt=1011):
    print(int(id))
    url = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{id}/")
    return json.loads(url.text)["name"]