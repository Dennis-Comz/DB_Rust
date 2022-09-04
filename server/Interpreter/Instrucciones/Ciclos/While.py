from Interpreter.Expresiones.Expresion import Expresion
from Interpreter.Instrucciones.Instruccion import Instruccion
from Interpreter.TablaSimbolos.TablaSimbolos import TablaSimbolos
from Interpreter.Driver.Driver import Driver
from Interpreter.TablaSimbolos.Tipos import Tipos
from static import simbs

class While(Instruccion):
    def __init__(self, condicion: Expresion, cuerpo, linea, columna):
        self.condicion = condicion
        self.cuerpo = cuerpo
        self.linea = linea
        self.columna = columna
    
    def ejecutar(self, driver: Driver, ts: TablaSimbolos, errores):
        try:
            ts_local = TablaSimbolos(ts, 'WHILE')
            tipoCondicion = self.condicion.getTipo(driver, ts, errores)
            valorCondicion = self.condicion.getValor(driver, ts, errores)

            if tipoCondicion != Tipos.BOOLEAN:
                driver.append(f"Error Semantico, la condicion a evaluar no es booleana, linea {self.linea} columna {self.columna}")
                raise Exception({"tipo":"Semantico", "descripcion":f"la condicion a evaluar no es booleana", "linea": str(self.linea), "columna":str(self.columna), "ambito": ts_local.env})

            while valorCondicion:
                retorno = self.cuerpo.ejecutar(driver, ts_local, errores)
                if retorno is not None:
                    if retorno["continue"]:
                        continue
                    elif retorno["break"]:
                        break
                    elif retorno["return"]:
                        simbs.append(ts_local)
                        return retorno
                valorCondicion = self.condicion.getValor(driver, ts, errores)
            simbs.append(ts_local)

        except Exception as d:
            if type(d.args[0]) == dict:
                errores.append(d.args[0])
            pass
