
import json
from fastapi import FastAPI , Path
import requests
from fastapi import Response


testAPI = FastAPI()

@testAPI.get("/")

async def req(id: str , gt=0, lt=1011):
    print(int(id))
    url = requests.get(f"https://unpkg.com/pokeapi-sprites@2.0.2/sprites/pokemon/other/dream-world/{id}.svg")
    return Response(content=image_bytes, media_type="image/svg")