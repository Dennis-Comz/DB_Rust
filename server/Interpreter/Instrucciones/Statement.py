from Interpreter.Instrucciones.Instruccion import Instruccion
from Interpreter.TablaSimbolos.TablaSimbolos import TablaSimbolos
from Interpreter.Driver.Driver import Driver

class Statement(Instruccion):

    def __init__(self, code, linea: int, columna: int):
        self.code = code
        self.linea = linea
        self.columna = columna

    def ejecutar(self, driver: Driver, ts: TablaSimbolos):
        for ins in self.code:
            ins.ejecutar(driver, ts)