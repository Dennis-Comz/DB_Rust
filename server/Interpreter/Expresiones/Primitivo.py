from Interpreter.Expresiones.Expresion import Expresion
from Interpreter.TablaSimbolos.Tipos import definirTipo


class Primitivo(Expresion):

    def __init__(self, primitivo, tipo, linea: int, columna: int):
        self.tipo = tipo
        self.primitivo = primitivo
        self.linea = linea
        self.columna = columna

    def getTipo(self, driver, ts):
        if self.tipo is None:
            value = self.getValor(driver, ts)
            return definirTipo(value)
        else:
            return self.tipo

    def getValor(self, driver, ts):
        value = self.primitivo
        return value