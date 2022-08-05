from enum import Enum
from xmlrpc.client import boolean


class Tipos(Enum):
    INT64 = 1
    FLOAT64 = 2
    BOOLEAN = 3

def getTipo(s: str):
    if s == "INT64":
        return Tipos.INT64
    if s == "FLOAT64":
        return Tipos.FLOAT64
    if s == "BOOLEAN":
        return Tipos.BOOLEAN


def definirTipo(value):
    if type(value) == float:
        return Tipos.FLOAT64
    elif type(value) == int:
        return Tipos.INT64
    elif type(value) == bool:
        return Tipos.BOOLEAN
    else:
        return None


class Tipo:

    def __init__(self, stipo: str):
        self.stipo = stipo
        self.tipo = getTipo(stipo)

    def getSTipo(self):
        return self.stipo