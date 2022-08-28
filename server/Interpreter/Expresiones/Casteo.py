from Interpreter.Expresiones.Expresion import Expresion
from Interpreter.TablaSimbolos.Tipos import definirTipo
from Interpreter.TablaSimbolos.Tipos import Tipos

class Casteo(Expresion):
    def __init__(self, exp: Expresion, tipo, linea, columna):
        self.exp = exp
        self.tipo = tipo
        self.linea = linea
        self.columna = columna

    def getTipo(self, driver, ts):
        return self.tipo

    def getValor(self, driver, ts):
        tipo = self.exp.getTipo(driver, ts)
        value = self.exp.getValor(driver, ts)
        if tipo != self.tipo:
            if self.tipo == Tipos.FLOAT64:
                return float(value)
            elif self.tipo == Tipos.INT64:
                return int(value)
            else:
                driver.console("Error no se puede castear")
        else:
            driver.console("Error no se puede castear al mismo tipo")