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
        ts_local = TablaSimbolos(ts, 'IF')
        condicion = self.condicion.getValor(driver, ts)
        tipo_condicion = self.condicion.getTipo(driver, ts)

        if tipo_condicion != Tipos.BOOLEAN:
            driver.append("Error Semantico, la condicion a evaluar no es booleana")
        
        if condicion:
            self.cuerpo.ejecutar(driver, ts_local)
        elif self.Else != None:
            self.Else.ejecutar(driver, ts_local)
    
    def getTipo(self, driver, ts):
        ts_local = TablaSimbolos(ts, 'IF')
        condicion = self.condicion.getValor(driver, ts)
        tipo_condicion = self.condicion.getTipo(driver, ts)

        if tipo_condicion != Tipos.BOOLEAN:
            driver.append("Error Semantico, la condicion a evaluar no es booleana")

        if condicion:
            return self.cuerpo.getTipo(driver, ts_local)
        elif self.Else != None:
            return self.Else.getTipo(driver, ts_local)

    def getValor(self, driver, ts):
        ts_local = TablaSimbolos(ts, 'IF')
        condicion = self.condicion.getValor(driver, ts)
        tipo_condicion = self.condicion.getTipo(driver, ts)

        if tipo_condicion != Tipos.BOOLEAN:
            driver.append("Error Semantico, la condicion a evaluar no es booleana")

        if condicion:
            return self.cuerpo.getValor(driver, ts_local)
        elif self.Else != None:
            return self.Else.getValor(driver, ts_local)