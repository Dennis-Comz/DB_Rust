from Interpreter.Expresiones.Expresion import Expresion
from Interpreter.Instrucciones.Instruccion import Instruccion
from Interpreter.TablaSimbolos.TablaSimbolos import TablaSimbolos
from Interpreter.Driver.Driver import Driver

class Statement(Instruccion, Expresion):

    def __init__(self, code, linea: int, columna: int):
        self.code = code
        self.linea = linea
        self.columna = columna

    def ejecutar(self, driver: Driver, ts: TablaSimbolos):
        for ins in self.code:
            ins.ejecutar(driver, ts)

    def getTipo(self, driver, ts):
        return super().getTipo(driver, ts)

    def getValor(self, driver, ts):
        return super().getValor(driver, ts)