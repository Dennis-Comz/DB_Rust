from Interpreter.TablaSimbolos.Tipos import Tipo
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

def getSimbolo(s):
    if s == 1:
        return Simbolos.VARIABLE