from Interpreter.Expresiones.Expresion import Expresion
from Interpreter.TablaSimbolos.Tipos import definirTipo

class Absoluto(Expresion):

    def __init__(self, exp: Expresion, linea, columna):
        self.exp = exp
        self.linea = linea
        self.columna = columna
    
    def getTipo(self, driver, ts):
        return self.exp.getTipo(driver, ts)

    def getValor(self, driver, ts):
        value = self.exp.getValor(driver, ts)
        if type(value) != int and type(value) != float:
            driver.append("tipo no valido")
            return
        if value < 0:
            value = value * (-1)
        return value