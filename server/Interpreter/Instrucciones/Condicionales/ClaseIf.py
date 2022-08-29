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

    def ejecutar(self, driver: Driver, ts: TablaSimbolos):
        try:
            ts_local = TablaSimbolos(ts, 'IF')
            condicion = self.condicion.getValor(driver, ts)
            tipo_condicion = self.condicion.getTipo(driver, ts)

            if tipo_condicion != Tipos.BOOLEAN:
                driver.append(f"Error Semantico, la condicion a evaluar no es booleana, linea {self.linea} columna {self.columna}")
                raise Exception(f"Error Semantico, la condicion a evaluar no es booleana, linea {self.linea} columna {self.columna}")
            
            if condicion:
                retorno = self.cuerpo.ejecutar(driver, ts_local)
                if retorno != None:
                    return retorno
            elif self.Else != None:
                retorno = self.Else.ejecutar(driver, ts_local)
                if retorno != None:
                    return retorno
        except:
            pass

    def getTipo(self, driver, ts):
        ts_local = TablaSimbolos(ts, 'IF')
        condicion = self.condicion.getValor(driver, ts)
        tipo_condicion = self.condicion.getTipo(driver, ts)

        if tipo_condicion != Tipos.BOOLEAN:
            driver.append(f"Error Semantico, la condicion a evaluar no es booleana, linea {self.linea} columna {self.columna}")
            raise Exception(f"Error Semantico, la condicion a evaluar no es booleana, linea {self.linea} columna {self.columna}")

        if self.cuerpo.getTipo(driver, ts_local) != self.Else.getTipo(driver, ts_local):
            driver.append(f"Error Semantico, los valores a retornar en if deben ser del mismo tipo, linea {self.linea} columna {self.columna}")
            raise Exception(f"Error Semantico, los valores a retornar en if deben ser del mismo tipo, linea {self.linea} columna {self.columna}")

        if condicion:
            return self.cuerpo.getTipo(driver, ts_local)
        elif self.Else != None:
            return self.Else.getTipo(driver, ts_local)

    def getValor(self, driver, ts):
        ts_local = TablaSimbolos(ts, 'IF')
        condicion = self.condicion.getValor(driver, ts)
        tipo_condicion = self.condicion.getTipo(driver, ts)

        if tipo_condicion != Tipos.BOOLEAN:
            driver.append(f"Error Semantico, la condicion a evaluar no es booleana, linea {self.linea} columna {self.columna}")
            raise Exception(f"Error Semantico, la condicion a evaluar no es booleana, linea {self.linea} columna {self.columna}")

        if condicion:
            return self.cuerpo.getValor(driver, ts_local)
        elif self.Else != None:
            return self.Else.getValor(driver, ts_local)