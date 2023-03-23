
import json
from fastapi import FastAPI , Path
import requests
from fastapi import Response


testAPI = FastAPI()

@testAPI.get("/")

async def req(id: str , gt=0, lt=1011):
    print(int(id))
    url = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{id}/")
    return Response(media_type="svg")