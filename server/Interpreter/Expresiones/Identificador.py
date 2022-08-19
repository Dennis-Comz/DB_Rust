from Interpreter.Driver.Driver import Driver
from Interpreter.Expresiones.Expresion import Expresion
from Interpreter.TablaSimbolos.TablaSimbolos import TablaSimbolos


class Identificador(Expresion):

    def __init__(self, identificador: str, linea: int, columna: int):
        self.columna = columna
        self.linea = linea
        self.identificador = identificador

    def getTipo(self, driver: Driver, ts: TablaSimbolos):
        return ts.buscar(self.identificador).tipo

    def getValor(self, driver: Driver, ts: TablaSimbolos):
        simbolo = ts.buscar(self.identificador)

        if simbolo is not None and simbolo.valor != None:
            return simbolo.valor
        elif simbolo.valor == None:
            driver.append(f"Variable no inicializada linea: {self.linea}, columna: {self.columna}")
            return            
        else:
            driver.append(f"No se encontró el símbolo linea: {self.linea}, columna: {self.columna}")
            return