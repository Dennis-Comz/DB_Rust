from Interpreter.Instrucciones.Instruccion import Instruccion

class Continue(Instruccion):
    def __init__(self, linea, columna):
        self.linea = linea
        self.columna = columna

    def ejecutar(self, driver, ts):
#       return break continue valorReturn 
        return {"return":False, "break":False, "continue":True, "valRetorno":None}