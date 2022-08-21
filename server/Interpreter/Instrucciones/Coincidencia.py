from typing import List
from Interpreter.Expresiones.Expresion import Expresion
from Interpreter.Instrucciones.Instruccion import Instruccion
from Interpreter.TablaSimbolos.TablaSimbolos import TablaSimbolos
from Interpreter.TablaSimbolos.Tipos import Tipos
from Interpreter.Driver.Driver import Driver

class Coincidencia(Instruccion):
    def __init__(self, valores, cuerpo: Instruccion, linea: int, columna: int):
        self.valores = valores
        self.cuerpo = cuerpo
        self.linea = linea
        self.columna = columna

    def ejecutar(self, driver: Driver, ts: TablaSimbolos):
        
        self.cuerpo.ejecutar(driver, ts);
    
    def getValores(self, driver, ts):
        vals = []
        
        if self.valores != []:
            for val in self.valores:
                vals.append(val.getValor(driver, ts))
        
        return vals

    def getTipos(self, driver, ts):
        types = []
        if self.valores != []:
            for val in self.valores:
                types.append(val.getTipo(driver, ts))
        
        return types
        

