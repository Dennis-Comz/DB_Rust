from Interpreter.TablaSimbolos.Simbolo import getSimbolo
from Interpreter.TablaSimbolos.Tipos import Tipos

class Clase:
    def __init__(self, simbolo:int, idClase:str, instrucciones):
        self.simbolo = getSimbolo(simbolo)
        self.idClase = idClase
        self.instrucciones = instrucciones