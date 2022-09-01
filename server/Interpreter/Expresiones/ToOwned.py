from Interpreter.Expresiones.Expresion import Expresion
from Interpreter.TablaSimbolos.Tipos import definirTipo, Tipos

class ToOwned(Expresion):

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
        if tipo != Tipos.STR_POINTER and tipo != Tipos.STR_BUFFER:
            driver.append(f'Error Semantico, tipo de dato no valido {tipo} se esperaba Tipos.STR_POINTER o Tipos.STR_BUFFER, linea {self.exp.linea}, columna {self.exp.columna}')
            raise Exception(f'Error Semantico, tipo de dato no valido {tipo} se esperaba Tipos.STR_POINTER o Tipos.STR_BUFFER, linea {self.exp.linea}, columna {self.exp.columna}')
        return value