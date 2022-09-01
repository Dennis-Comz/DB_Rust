from Interpreter.Instrucciones.Instruccion import Instruccion

class Break(Instruccion):
    def __init__(self, exp, linea, columna):
        self.exp = exp
        self.linea = linea
        self.columna = columna

    def ejecutar(self, driver, ts):
        if self.exp == None:
            return {"return":False, "break":True, "continue":False, "expTipo":"", "expValor":""}
        expTipo = self.exp.getTipo(driver,ts)
        expValor = self.exp.getValor(driver, ts)
        return {"return":False, "break":True, "continue":False, "expTipo": expTipo, "expValor": expValor}