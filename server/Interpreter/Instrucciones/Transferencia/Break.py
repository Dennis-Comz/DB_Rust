from Interpreter.Instrucciones.Instruccion import Instruccion

class Break(Instruccion):
    def __init__(self, exp, linea, columna):
        self.exp = exp
        self.linea = linea
        self.columna = columna

    def ejecutar(self, driver, ts):
        if self.exp == None:
            return {"return":False, "break":True, "continue":False, "expRetorno":None}
        return {"return":False, "break":True, "continue":False, "expRetorno":self.exp}