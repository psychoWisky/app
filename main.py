
import json
from fastapi import FastAPI 
import requests


testAPI = FastAPI()

@testAPI.get("/requests")

async def req(name:str):
    url = requests.get(f"https://pokeapi.co/api/v2/evolution-chain/{name}/")
    return [i["name"] for i in json.loads(url.text)]