from enum import Enum

class Simbolo:

    def __init__(self, simbolo: int, mutable, id: str, tipo, valor):
        self.simbolo = getSimbolo(simbolo)
        self.mutable = mutable
        self.id = id
        self.tipo = tipo
        self.valor = valor

class Simbolos(Enum):
    VARIABLE = 1
    FUNCION = 2

def getSimbolo(s):
    if s == 1:
        return Simbolos.VARIABLE
    elif s == 2:
        return Simbolos.FUNCION