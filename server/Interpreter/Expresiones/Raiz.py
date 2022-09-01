import math
from Interpreter.Expresiones.Expresion import Expresion
from Interpreter.TablaSimbolos.Tipos import definirTipo, Tipos

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
        tipo = self.exp.getTipo(driver, ts)
        value = self.exp.getValor(driver, ts)
        if tipo != Tipos.FLOAT64:
            driver.append(f'Error Semantico, no se puede obtener raiz de {tipo}, linea {self.exp.linea}, columna {self.exp.columna}')
            raise Exception(f'Error Semantico, no se puede obtener raiz de {tipo}, linea {self.exp.linea}, columna {self.exp.columna}')
        if value < 0:
            driver.append(f'Error Semantico, RESULTADO INDEFINIDO, no se pueden obtener raices negativas, linea {self.exp.linea}, columna {self.exp.columna}')
            raise Exception(f'Error Semantico, RESULTADO INDEFINIDO, no se pueden obtener raices negativas, linea {self.exp.linea}, columna {self.exp.columna}')
        return math.sqrt(value)