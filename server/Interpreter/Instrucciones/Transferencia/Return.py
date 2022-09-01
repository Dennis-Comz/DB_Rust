from Interpreter.Instrucciones.Instruccion import Instruccion

class Return(Instruccion):
    def __init__(self, exp, linea, columna):
        self.exp = exp
        self.linea = linea
        self.columna = columna

    def ejecutar(self, driver, ts):
        if self.exp == None:
            return None
        expTipo = self.exp.getTipo(driver,ts)
        expValor = self.exp.getValor(driver, ts)
        return {"return":True, "break":False, "continue":False, "expTipo": expTipo, "expValor": expValor}