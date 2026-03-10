from fastapi import FastAPI
from enum import Enum, auto
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


class Material(Enum):
    bronce = auto()
    plata = auto()
    oro = auto()


class caballeros(BaseModel):
    id: int
    name: str
    material: Material
    attack: int
    constelacion: str


caballero1 = caballeros(id=1, name="Pepe", material=Material.plata, attack=300, constelacion="acuario")
caballero2 = caballeros(id=2, name="Carlitos", material=Material.oro, attack=200, constelacion="leo")

lista_caballeros = [caballero1, caballero2]


@app.get("/showCaballero/{id}")
def ShowCaballeros(id: int):
    for c in lista_caballeros:
        if c.id == id:
            return {
                "caballero": c.name,
                "id": c.id,
                "constelacion": c.constelacion,
                "ataque": c.attack,
                "material": c.material.name
            }


@app.get("/fightCaballero/{id}")
def fightCaballero(id: int):
    for c in lista_caballeros:
        if c.id == id:
            for enemigo in lista_caballeros:
                if enemigo.id != id:
                    if c.attack > enemigo.attack:
                        return {"resultado": f"{c.name} gana contra {enemigo.name}"}
                    elif c.attack < enemigo.attack:
                        return {"resultado": f"{enemigo.name} gana contra {c.name}"}
                    else:
                        return {"resultado": "Empate"}


@app.get("/ShowConstelacion")
def ShowConstelacion():
    constelaciones = []
    for c in lista_caballeros:
        constelaciones.append(c.constelacion)
    return {"constelaciones": constelaciones}


@app.get("/YourCaballero")
def YourCaballero():
    c = lista_caballeros[0]
    return {
        "tu_caballero": c.name,
        "constelacion": c.constelacion,
        "ataque": c.attack
    }

@app.get("/showallcaballeros")
def showallcaballeros():
    return {"caballeros": lista_caballeros}