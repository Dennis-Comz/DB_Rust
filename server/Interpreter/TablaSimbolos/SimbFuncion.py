from Interpreter.TablaSimbolos.Simbolo import getSimbolo
from Interpreter.TablaSimbolos.Tipos import Tipos

class SimbFuncion:
                                          #Array de objetos tipo parametro
                                                    # |
    def __init__(self, simbolo: int, nombre:str, parametros, tipo:Tipos, cuerpo):
        self.simbolo = getSimbolo(simbolo)
        self.nombre = nombre
        self.parametros = parametros
        self.tipo = tipo
        self.cuerpo = cuerpo