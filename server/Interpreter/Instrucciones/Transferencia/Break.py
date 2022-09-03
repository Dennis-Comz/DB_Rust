from Interpreter.Instrucciones.Instruccion import Instruccion
from Interpreter.Expresiones.Expresion import Expresion

class Break(Instruccion, Expresion):
    def __init__(self, exp, linea, columna):
        self.exp = exp
        self.linea = linea
        self.columna = columna

    def ejecutar(self, driver, ts, errores):
        if self.exp == None:
            return {"return":False, "break":True, "continue":False, "expTipo":"", "expValor":""}
        expTipo = self.exp.getTipo(driver,ts, errores)
        expValor = self.exp.getValor(driver, ts, errores)
        return {"return":False, "break":True, "continue":False, "expTipo": expTipo, "expValor": expValor}

    def getTipo(self, driver, ts, errores):
        if self.exp == None:
            return {"return":False, "break":True, "continue":False, "expTipo":"", "expValor":""}
        expTipo = self.exp.getTipo(driver,ts, errores)
        expValor = self.exp.getValor(driver, ts, errores)
        return {"return":False, "break":True, "continue":False, "expTipo": expTipo, "expValor": expValor}

    def getValor(self, driver, ts, errores):
        if self.exp == None:
            return {"return":False, "break":True, "continue":False, "expTipo":"", "expValor":""}
        expTipo = self.exp.getTipo(driver,ts, errores)
        expValor = self.exp.getValor(driver, ts, errores)
        return {"return":False, "break":True, "continue":False, "expTipo": expTipo, "expValor": expValor}
