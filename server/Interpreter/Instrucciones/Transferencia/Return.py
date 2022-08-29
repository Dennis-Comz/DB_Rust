from Interpreter.Instrucciones.Instruccion import Instruccion

class Return(Instruccion):
    def __init__(self, exp, linea, columna):
        self.exp = exp
        self.linea = linea
        self.columna = columna

    def ejecutar(self, driver, ts):
        if self.exp == None:
            return None
        valorRetorno = self.exp.getValor(driver, ts)
#               return break continue valorReturn 
        return {"return":True, "break":False, "continue":False, "valRetorno":valorRetorno}