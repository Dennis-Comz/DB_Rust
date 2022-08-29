from Interpreter.Instrucciones.Instruccion import Instruccion

class Break(Instruccion):
    def __init__(self, linea, columna):
        self.linea = linea
        self.columna = columna

    def ejecutar(self, driver, ts):
#       return break continue valorReturn 
        return {"return":False, "break":True, "continue":False, "valRetorno":None}