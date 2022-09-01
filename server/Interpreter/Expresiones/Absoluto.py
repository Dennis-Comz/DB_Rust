from Interpreter.Expresiones.Expresion import Expresion
from Interpreter.TablaSimbolos.Tipos import Tipos

class Absoluto(Expresion):

    def __init__(self, exp: Expresion, linea, columna):
        self.exp = exp
        self.linea = linea
        self.columna = columna
    
    def getTipo(self, driver, ts):
        return self.exp.getTipo(driver, ts)

    def getValor(self, driver, ts):
        tipo = self.exp.getTipo(driver, ts)
        value = self.exp.getValor(driver, ts)
        if tipo != Tipos.INT64 and tipo != Tipos.FLOAT64:
            driver.append(f'Error Semantico, no se puede obtener valor absoluto de tipo {tipo}, linea {self.exp.linea}, columna {self.exp.columna}')
            raise Exception(f'Error Semantico, no se puede obtener valor absoluto de tipo {tipo}, linea {self.exp.linea}, columna {self.exp.columna}')
        if value < 0:
            value = value * (-1)
        return value