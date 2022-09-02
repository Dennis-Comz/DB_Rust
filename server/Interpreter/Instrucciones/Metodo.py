from Interpreter.Instrucciones.Instruccion import Instruccion
from Interpreter.Driver.Driver import Driver
from Interpreter.TablaSimbolos.TablaSimbolos import TablaSimbolos
from Interpreter.TablaSimbolos.Funcion import Funcion

class Metodo(Instruccion):
                            #Array de objetos tipo parametro
                                        # |
    def __init__(self, nombre:str, parametros, tipo, cuerpo:Instruccion, simbolo: Funcion, linea:int, columna:int):
        self.nombre = nombre
        self.parametros = parametros
        self.tipo = tipo
        self.cuerpo = cuerpo
        self.simbolo = simbolo
        self.linea = linea
        self.columna = columna
    
    def ejecutar(self, driver: Driver, ts: TablaSimbolos):
        existe = ts.buscarFuncion(self.nombre)
        if existe is None:
            ts.addFuncion(self.nombre, self.simbolo)