from Interpreter.Expresiones.Expresion import Expresion
from Interpreter.TablaSimbolos.Tipos import Tipos

class Absoluto(Expresion):

    def __init__(self, exp: Expresion, linea, columna):
        self.exp = exp
        self.linea = linea
        self.columna = columna
    
    def getTipo(self, driver, ts, errores):
        return self.exp.getTipo(driver, ts, errores)

    def getValor(self, driver, ts, errores):
        tipo = self.exp.getTipo(driver, ts, errores)
        value = self.exp.getValor(driver, ts, errores)
        if tipo != Tipos.INT64 and tipo != Tipos.FLOAT64:
            driver.append(f'Error Semantico, no se puede obtener valor absoluto de tipo {tipo}, linea {self.exp.linea}, columna {self.exp.columna}')
            raise Exception({"tipo":"Semantico", "descripcion":f"no se puede obtener valor absoluto de tipo {tipo}", "linea": str(self.exp.linea), "columna":str(self.exp.columna), "ambito": ts.env})
        if value < 0:
            value = value * (-1)
        return value