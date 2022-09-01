from Interpreter.Expresiones.Expresion import Expresion
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
        #CONVERSIONES DE INT A TIPOS VALIDOS
        if self.tipo == Tipos.INT64 and tipo == Tipos.INT64:
            return int(value)
        elif self.tipo == Tipos.FLOAT64 and tipo == Tipos.INT64:
            return float(value)
        elif self.tipo == Tipos.CARACTER and tipo == Tipos.INT64:
            return chr(value)
        #CONVERSIONES DE FLOAT A TIPOS VALIDOS
        elif self.tipo == Tipos.INT64 and tipo == Tipos.FLOAT64:
            return int(value)
        elif self.tipo == Tipos.FLOAT64 and tipo == Tipos.FLOAT64:
            return float(value)
        #CONVERSIONES DE CHAR A TIPOS VALIDOS
        elif self.tipo == Tipos.INT64 and tipo == Tipos.CARACTER:
            return int(value)
        elif self.tipo == Tipos.CARACTER and tipo == Tipos.CARACTER:
            return chr(value)
        #CONVERSIONES DE STRING A TIPOS VALIDOS
        elif self.tipo == Tipos.STR_BUFFER and tipo == Tipos.STR_BUFFER:
            return value
        #CONVERSIONES DE &STR A TIPOS VALIDOS
        elif self.tipo == Tipos.STR_POINTER and tipo == Tipos.STR_POINTER:
            return value
        else:
            driver.append(f'Error Semantico, No se puede castear {tipo} a {self.tipo}, linea {self.exp.linea}, columna {self.exp.columna}')
            raise Exception(f'Error Semantico, No se puede castear {tipo} a {self.tipo}, linea {self.exp.linea}, columna {self.exp.columna}')