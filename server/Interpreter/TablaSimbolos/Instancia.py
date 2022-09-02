from Interpreter.TablaSimbolos.Simbolo import getSimbolo
from Interpreter.TablaSimbolos.Tipos import Tipos

class Instancia:
    def __init__(self, simbolo:int, idClase:str, idInstancia:str, entorno, tipo:Tipos):
        self.simbolo = getSimbolo(simbolo)
        self.idClase = idClase
        self.idInstancia = idInstancia
        self.entorno = entorno
        self.tipo = tipo