from lib2to3.pgen2.token import OP
from Interpreter.Expresiones.Operaciones.OperacionLogica import OperacionLogica, Operador, getOperacion
from Interpreter.TablaSimbolos.Tipos import Tipos, definirTipo

class Logicas(OperacionLogica):

    def getTipo(self, driver, ts):
        value = self.getValor(driver, ts)
        return definirTipo(value)
    
    def getValor(self, driver, ts):
        tipo_exp1 = None
        if self.exp1 != None:
            tipo_exp1 = self.exp1.getTipo(driver, ts)
        tipo_exp2 = self.exp2.getTipo(driver, ts)
        
        if tipo_exp1 != None:
            if tipo_exp1 == Tipos.BOOLEAN and tipo_exp2 == Tipos.BOOLEAN:
                if self.operador == Operador.AND:
                    return self.exp1.getValor(driver, ts) and self.exp2.getValor(driver, ts)
                elif self.operador == Operador.OR:
                    return self.exp1.getValor(driver, ts) or self.exp2.getValor(driver, ts)
            else:
                driver.append(f'No se pueden comparar {tipo_exp1} con {tipo_exp2}, linea {self.exp2.linea}, columna {self.exp2.columna}')
        else:
            if tipo_exp2 == Tipos.BOOLEAN:
                if self.operador == Operador.NOT:
                    return not self.exp2.getValor(driver, ts)
            else:
                driver.append(f'No se puede negar {tipo_exp2}, linea {self.exp2.linea}, columna {self.exp2.columna}')