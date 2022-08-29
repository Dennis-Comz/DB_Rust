from Interpreter.Expresiones.Expresion import Expresion
from Interpreter.Instrucciones.Instruccion import Instruccion
from Interpreter.TablaSimbolos.TablaSimbolos import TablaSimbolos
from Interpreter.Driver.Driver import Driver

class While(Instruccion):
    def __init__(self, condicion, cuerpo, linea, columna):
        self.condicion = condicion
        self.cuerpo = cuerpo
        self.linea = linea
        self.columna = columna
    
    def ejecutar(self, driver: Driver, ts: TablaSimbolos):
        return super().ejecutar(driver, ts)