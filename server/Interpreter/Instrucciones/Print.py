from Interpreter.Instrucciones.Instruccion import Instruccion
from Interpreter.Expresiones.Expresion import Expresion

class Print(Instruccion):
    def __init__(self, exp: Expresion, linea, columna):
        self.columna = columna
        self.linea = linea
        self.exp = exp

    def ejecutar(self, driver, ts):
        driver.append(str(self.exp.getValor(driver, ts)))