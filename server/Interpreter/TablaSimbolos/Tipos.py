from enum import Enum
from xmlrpc.client import boolean


class Tipos(Enum):
    INT64 = 1
    FLOAT64 = 2
    BOOLEAN = 3
    CARACTER = 4
    STR_BUFFER = 5
    STR_POINTER = 6
    VOID = 7
    OBJETO = 8

def getTipo(s: str):
    if s == "INT64":
        return Tipos.INT64
    if s == "FLOAT64":
        return Tipos.FLOAT64
    if s == "BOOLEAN":
        return Tipos.BOOLEAN
    if s == "CARACTER":
        return Tipos.CARACTER
    if s == "STR_BUFFER":
        return Tipos.STR_BUFFER
    if s == "STR_POINTER":
        return Tipos.STR_POINTER

def definirTipo(value):
    if type(value) == float:
        return Tipos.FLOAT64
    elif type(value) == int:
        return Tipos.INT64
    elif type(value) == bool:
        return Tipos.BOOLEAN
    elif type(value) == str:
        return Tipos.STR_BUFFER
    else:
        return None


class Tipo:

    def __init__(self, stipo: str):
        self.stipo = stipo
        self.tipo = getTipo(stipo)

    def getSTipo(self):
        return self.stipo