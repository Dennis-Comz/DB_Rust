from Interpreter.TablaSimbolos.Simbolo import getSimbolo
from Interpreter.TablaSimbolos.Tipos import Tipos

class Arreglo:
    def __init__(self, simbolo:int, mutable:bool, id:str, tipo:Tipos, dimensiones:list, valores:list):
        self.simbolo = simbolo
        self.mutable = mutable
        self.id = id
        self.tipo = tipo
        self.dimensiones = dimensiones
        self.valores = valores
