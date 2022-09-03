from Interpreter.Driver.Driver import Driver
from Interpreter.Expresiones.Expresion import Expresion
from Interpreter.TablaSimbolos.TablaSimbolos import TablaSimbolos
from Interpreter.TablaSimbolos.Tipos import Tipos

class Identificador(Expresion):

    def __init__(self, identificador: str, linea: int, columna: int):
        self.columna = columna
        self.linea = linea
        self.identificador = identificador

    def getTipo(self, driver: Driver, ts: TablaSimbolos, errores):
        val = ts.buscar(self.identificador)
        if val is not None:
            return val.tipo
        else:
            driver.append(f'Error Semantico, No se encontró el símbolo, linea {self.linea}, columna {self.columna}')
            raise Exception({"tipo":"Semantico", "descripcion":f"No se encontró el símbolo", "linea": str(self.linea), "columna":str(self.columna)})

    def getValor(self, driver: Driver, ts: TablaSimbolos, errores):
        simbolo = ts.buscar(self.identificador)

        if simbolo is not None:
            if simbolo.valor is not None:
                return simbolo.valor
            else:
                driver.append(f'Error Semantico, variable no inicializada, linea {self.linea}, columna {self.columna}')
                raise Exception({"tipo":"Semantico", "descripcion":f"variable no inicializada", "linea": str(self.linea), "columna":str(self.columna)})            
        else:
            driver.append(f'Error Semantico, No se encontró el símbolo, linea {self.linea}, columna {self.columna}')
            raise Exception({"tipo":"Semantico", "descripcion":f"No se encontró el símbolo", "linea": str(self.linea), "columna":str(self.columna)})