from Interpreter.Instrucciones.Instruccion import Instruccion
from Interpreter.Driver.Driver import Driver
from Interpreter.TablaSimbolos.TablaSimbolos import TablaSimbolos
from Interpreter.TablaSimbolos.SimbFuncion import SimbFuncion

class Metodo(Instruccion):
                            #Array de objetos tipo parametro
                                        # |
    def __init__(self, nombre:str, parametros, tipo, cuerpo:Instruccion, simbolo: SimbFuncion, linea:int, columna:int):
        self.nombre = nombre
        self.parametros = parametros
        self.tipo = tipo
        self.cuerpo = cuerpo
        self.simbolo = simbolo
        self.linea = linea
        self.columna = columna
    
    def ejecutar(self, driver: Driver, ts: TablaSimbolos):
        ts.addFuncion(self.nombre, self.simbolo)