import math
from Interpreter.Expresiones.Expresion import Expresion
from Interpreter.TablaSimbolos.Tipos import definirTipo

class Raiz(Expresion):

    def __init__(self, exp: Expresion, tipo, linea, columna):
        self.exp = exp
        self.tipo = tipo
        self.linea = linea
        self.columna = columna
    
    def getTipo(self, driver, ts):
        if self.tipo is None:
            value = self.getValor(driver, ts)
            return definirTipo(value)
        else:
            return self.tipo

    def getValor(self, driver, ts):
        value = self.exp.getValor(driver, ts)
        if type(value) != float:
            driver.append("tipo no valido")
            return
        if value < 0:
            driver.append("No se pueden obtener raices negativas")
            return
        return math.sqrt(value)