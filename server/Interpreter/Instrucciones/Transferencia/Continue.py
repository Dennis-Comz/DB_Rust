from Interpreter.Instrucciones.Instruccion import Instruccion
from Interpreter.Expresiones.Expresion import Expresion

class Continue(Instruccion, Expresion):
    def __init__(self, linea, columna):
        self.linea = linea
        self.columna = columna

    def ejecutar(self, driver, ts, errores):
        return {"return":False, "break":False, "continue":True, "expTipo":"", "expValor":""}

    def getTipo(self, driver, ts, errores):
        return {"return":False, "break":False, "continue":True, "expTipo":"", "expValor":""}

    def getValor(self, driver, ts, errores):
        return {"return":False, "break":False, "continue":True, "expTipo":"", "expValor":""}
