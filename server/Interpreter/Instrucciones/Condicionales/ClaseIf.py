from Interpreter.Expresiones.Expresion import Expresion
from Interpreter.Instrucciones.Instruccion import Instruccion
from Interpreter.TablaSimbolos.TablaSimbolos import TablaSimbolos
from Interpreter.TablaSimbolos.Tipos import Tipos
from Interpreter.Driver.Driver import Driver

class ClaseIf(Instruccion, Expresion):
    def __init__(self, condicion: Expresion, cuerpo: Instruccion, Else, linea: int, columna: int):
        self.condicion = condicion
        self.cuerpo = cuerpo
        self.Else = Else
        self.linea = linea
        self.columna = columna

    def ejecutar(self, driver: Driver, ts: TablaSimbolos, errores):
        try:
            ts_local = TablaSimbolos(ts, 'IF')

            condicion = self.condicion.getValor(driver, ts, errores)
            tipo_condicion = self.condicion.getTipo(driver, ts, errores)

            if tipo_condicion != Tipos.BOOLEAN:
                driver.append(f"Error Semantico, la condicion a evaluar no es booleana, linea {self.linea} columna {self.columna}")
                raise Exception({"tipo":"Semantico", "descripcion":f"la condicion a evaluar no es booleana", "linea": str(self.linea), "columna":str(self.columna)})
            
            if condicion:
                retorno = self.cuerpo.ejecutar(driver, ts_local, errores)
                return retorno
            elif self.Else != None:
                retorno = self.Else.ejecutar(driver, ts_local, errores)
                return retorno
        except Exception as d:
            if type(d.args[0]) == dict:
                errores.append(d.args[0])
            pass
        
    def getTipo(self, driver, ts, errores):
        ts_local = TablaSimbolos(ts, 'IF')
        condicion = self.condicion.getValor(driver, ts, errores)
        tipo_condicion = self.condicion.getTipo(driver, ts, errores)

        if tipo_condicion != Tipos.BOOLEAN:
            driver.append(f"Error Semantico, la condicion a evaluar no es booleana, linea {self.linea} columna {self.columna}")
            raise Exception({"tipo":"Semantico", "descripcion":f"la condicion a evaluar no es booleana", "linea": str(self.linea), "columna":str(self.columna)})

        if self.cuerpo.getTipo(driver, ts_local, errores) != self.Else.getTipo(driver, ts_local, errores):
            driver.append(f"Error Semantico, los valores a retornar en if deben ser del mismo tipo, linea {self.linea} columna {self.columna}")
            raise Exception({"tipo":"Semantico", "descripcion":f"los valores a retornar en if deben ser del mismo tipo", "linea": str(self.linea), "columna":str(self.columna)})

        if condicion:
            return self.cuerpo.getTipo(driver, ts_local, errores)
        elif self.Else != None:
            return self.Else.getTipo(driver, ts_local, errores)

    def getValor(self, driver, ts, errores):
        ts_local = TablaSimbolos(ts, 'IF')
        tipo_condicion = self.condicion.getTipo(driver, ts, errores)
        condicion = self.condicion.getValor(driver, ts, errores)

        if tipo_condicion != Tipos.BOOLEAN:
            driver.append(f"Error Semantico, la condicion a evaluar no es booleana, linea {self.linea} columna {self.columna}")
            raise Exception({"tipo":"Semantico", "descripcion":f"la condicion a evaluar no es booleana", "linea": str(self.linea), "columna":str(self.columna)})

        if condicion:
            return self.cuerpo.getValor(driver, ts_local, errores)
        elif self.Else != None:
            return self.Else.getValor(driver, ts_local, errores)