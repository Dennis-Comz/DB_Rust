import traceback
from Interpreter.Expresiones.Expresion import Expresion
from Interpreter.Instrucciones.Instruccion import Instruccion
from Interpreter.TablaSimbolos.TablaSimbolos import TablaSimbolos
from Interpreter.Driver.Driver import Driver

class Statement(Instruccion, Expresion):

    def __init__(self, code, linea: int, columna: int):
        self.code = code
        self.linea = linea
        self.columna = columna

    def ejecutar(self, driver: Driver, ts: TablaSimbolos):
        result = {"return":False, "break":False, "continue":False, "valRetorno":None}

        for ins in self.code:
            retorno = ins.ejecutar(driver, ts)
            if retorno != None:
                result["valRetorno"] = retorno["valRetorno"]
                if retorno["break"]:
                    result["break"] = True
                    return result
                elif retorno["continue"]:
                    result["continue"] = True
                    return result
                elif retorno["return"]:
                    result["return"] = True
                    return result


    def getTipo(self, driver, ts):
        for ins in self.code:
            if getattr(ins, "ejecutar", None) != None:
                ins.ejecutar(driver, ts)
        return self.code[(len(self.code)-1)].getTipo(driver, ts)

    def getValor(self, driver, ts):
        return self.code[(len(self.code)-1)].getValor(driver, ts)