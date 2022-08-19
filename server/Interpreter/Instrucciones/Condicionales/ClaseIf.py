from Interpreter.Expresiones.Expresion import Expresion
from Interpreter.Instrucciones.Instruccion import Instruccion
from Interpreter.TablaSimbolos.TablaSimbolos import TablaSimbolos
from Interpreter.TablaSimbolos.Tipos import Tipos
from Interpreter.Driver.Driver import Driver

class ClaseIf(Instruccion):
    def __init__(self, condicion: Expresion, cuerpo: Instruccion, Else, linea: int, columna: int):
        self.condicion = condicion
        self.cuerpo = cuerpo
        self.Else = Else
        self.linea = linea
        self.columna = columna

    def ejecutar(self, driver: Driver, ts: TablaSimbolos):
        condicion = self.condicion.getValor(driver, ts)
        tipo_condicion = self.condicion.getTipo(driver, ts)

        if tipo_condicion != Tipos.BOOLEAN:
            driver.append("Error Semantico, la condicion a evaluar no es booleana")
        
        if condicion:
            self.cuerpo.ejecutar(driver, ts, 'IF')
        elif self.Else != None:
            self.Else.ejecutar(driver, ts, 'IF')

        print(ts.env)