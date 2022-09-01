from Interpreter.Driver.Driver import Driver
from Interpreter.Expresiones.Expresion import Expresion
from Interpreter.TablaSimbolos.TablaSimbolos import TablaSimbolos


class Identificador(Expresion):

    def __init__(self, identificador: str, linea: int, columna: int):
        self.columna = columna
        self.linea = linea
        self.identificador = identificador

    def getTipo(self, driver: Driver, ts: TablaSimbolos):
        val = ts.buscar(self.identificador).tipo
        return val

    def getValor(self, driver: Driver, ts: TablaSimbolos):
        simbolo = ts.buscar(self.identificador)

        if simbolo is not None and simbolo.valor != None:
            return simbolo.valor
        elif simbolo.valor == None:
            driver.append(f'Error Semantico, variable no inicializada, linea {self.linea}, columna {self.columna}')
            raise Exception(f'Error Semantico, variable no inicializada, linea {self.linea}, columna {self.columna}')            
        else:
            driver.append(f'Error Semantico, No se encontró el símbolo, linea {self.linea}, columna {self.columna}')
            raise Exception(f'Error Semantico, No se encontró el símbolo, linea {self.linea}, columna {self.columna}')