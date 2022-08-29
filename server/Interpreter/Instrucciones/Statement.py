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
        self.result = {"return":False, "break":False, "continue":False, "expRetorno":None}

    def ejecutar(self, driver: Driver, ts: TablaSimbolos):
        result = {"return":False, "break":False, "continue":False, "expRetorno":None}

        for ins in self.code:
            retorno = ins.ejecutar(driver, ts)
            if retorno != None:
                result["expRetorno"] = retorno["expRetorno"]
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
                retorno = ins.ejecutar(driver, ts)
                if retorno != None:
                    self.result["expRetorno"] = retorno["expRetorno"]
                    if retorno["break"]:
                        self.result["break"] = True
                        return self.result["expRetorno"].getTipo(driver, ts)
                    elif retorno["continue"]:
                        self.result["continue"] = True
                        return self.result
                    elif retorno["return"]:
                        self.result["return"] = True
                        return self.result["expRetorno"].getTipo(driver, ts)
        if getattr(self.code[(len(self.code)-1)], "getTipo", None) != None:
            return self.code[(len(self.code)-1)].getTipo(driver, ts)

    def getValor(self, driver, ts):
        if self.result["expRetorno"] != None:
            return self.result["expRetorno"].getValor(driver, ts)
        return self.code[(len(self.code)-1)].getValor(driver, ts)