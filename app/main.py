from fastapi import FastAPI
from random import randint
from pydantic import BaseModel
import socket

app = FastAPI()

# store stats as int
class StatBlock(BaseModel):
    stren: int
    dex: int
    con: int
    intell: int
    wis: int
    cha: int
    host: str

# roll 3d6 
def roll_stat():
    return sum(randint(1,6) for _ in range(3))

@app.get("/roll", response_model=StatBlock)
def roll():

    return StatBlock(
        stren = roll_stat(),
        dex = roll_stat(),
        con =roll_stat(),
        intell = roll_stat(),
        wis = roll_stat(),
        cha = roll_stat(),
        host = socket.gethostname() 
    )

