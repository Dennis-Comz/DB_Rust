from lib2to3.pgen2.token import OP
from Interpreter.Expresiones.Operaciones.OperacionLogica import OperacionLogica, Operador, getOperacion
from Interpreter.TablaSimbolos.Tipos import Tipos, definirTipo

class Logicas(OperacionLogica):

    def getTipo(self, driver, ts, errores):
        value = self.getValor(driver, ts, errores)
        return definirTipo(value)
    
    def getValor(self, driver, ts, errores):
        tipo_exp1 = None
        if self.exp1 != None:
            tipo_exp1 = self.exp1.getTipo(driver, ts, errores)
        tipo_exp2 = self.exp2.getTipo(driver, ts, errores)
        
        if tipo_exp1 != None:
            if tipo_exp1 == Tipos.BOOLEAN and tipo_exp2 == Tipos.BOOLEAN:
                if self.operador == Operador.AND:
                    return self.exp1.getValor(driver, ts, errores) and self.exp2.getValor(driver, ts, errores)
                elif self.operador == Operador.OR:
                    return self.exp1.getValor(driver, ts, errores) or self.exp2.getValor(driver, ts, errores)
            else:
                driver.append(f'Error Semantico, No se pueden comparar {tipo_exp1} con {tipo_exp2}, linea {self.exp2.linea}, columna {self.exp2.columna}')
                raise Exception({"tipo":"Semantico", "descripcion":f"No se pueden comparar {tipo_exp1} con {tipo_exp2}", "linea": str(self.exp2.linea), "columna":str(self.exp2.columna), "ambito": ts.env})
        else:
            if tipo_exp2 == Tipos.BOOLEAN:
                if self.operador == Operador.NOT:
                    return not self.exp2.getValor(driver, ts, errores)
            else:
                driver.append(f'Error Semantico, No se puede negar {tipo_exp2}, linea {self.exp2.linea}, columna {self.exp2.columna}')
                raise Exception({"tipo":"Semantico", "descripcion":f"No se puede negar {tipo_exp2}", "linea": str(self.exp2.linea), "columna":str(self.exp2.columna), "ambito": ts.env})