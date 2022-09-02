from Interpreter.Expresiones.Expresion import Expresion
from Interpreter.Instrucciones.Instruccion import Instruccion
from Interpreter.TablaSimbolos.TablaSimbolos import TablaSimbolos
from Interpreter.Driver.Driver import Driver
from Interpreter.TablaSimbolos.Tipos import Tipos

class While(Instruccion):
    def __init__(self, condicion: Expresion, cuerpo, linea, columna):
        self.condicion = condicion
        self.cuerpo = cuerpo
        self.linea = linea
        self.columna = columna
    
    def ejecutar(self, driver: Driver, ts: TablaSimbolos):
        try:
            result = {"return":False, "break":False, "continue":False, "expRetorno":None}
            ts_local = TablaSimbolos(ts, 'WHILE')
            tipoCondicion = self.condicion.getTipo(driver, ts)
            valorCondicion = self.condicion.getValor(driver, ts)

            if tipoCondicion != Tipos.BOOLEAN:
                driver.append(f"Error Semantico, la condicion a evaluar no es booleana, linea {self.linea} columna {self.columna}")
                raise Exception(f"Error Semantico, la condicion a evaluar no es booleana, linea {self.linea} columna {self.columna}")

            while valorCondicion:
                retorno = self.cuerpo.ejecutar(driver, ts_local)
                if retorno is not None:
                    if retorno["continue"]:
                        continue
                    elif retorno["break"]:
                        break
                    elif retorno["return"]:
                        return retorno
                valorCondicion = self.condicion.getValor(driver, ts)

        except:
            pass