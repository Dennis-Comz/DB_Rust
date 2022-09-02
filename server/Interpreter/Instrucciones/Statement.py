import traceback
from Interpreter.Expresiones.Expresion import Expresion
from Interpreter.Instrucciones.Instruccion import Instruccion
from Interpreter.TablaSimbolos.TablaSimbolos import TablaSimbolos
from Interpreter.Driver.Driver import Driver

class Statement(Instruccion, Expresion):
    array = []
    

    def __init__(self, code, linea: int, columna: int):
        self.code = code
        self.linea = linea
        self.columna = columna

    def ejecutar(self, driver: Driver, ts: TablaSimbolos):
        result = {"return":False, "break":False, "continue":False, "expTipo":"", "expValor": ""}

        try:
            for ins in self.code:
                retorno = ins.ejecutar(driver, ts)
                if retorno is not None:
                    result["expTipo"] = retorno["expTipo"]
                    result["expValor"] = retorno["expValor"]
                    if retorno["break"]:
                        result["break"] = True
                        return result
                    elif retorno["continue"]:
                        result["continue"] = True
                        return result
                    elif retorno["return"]:
                        result["return"] = True
                        return result
        except:
            pass

    def getTipo(self, driver, ts):
        result = {"return":False, "break":False, "continue":False, "expTipo":"", "expValor": ""}

        if getattr(self.code[(len(self.code)-1)], "getTipo", None) != None:
            return self.code[(len(self.code)-1)].getTipo(driver, ts)
        retorno = self.ejecutar(driver, ts)
        if result["expTipo"] == "":
            result = retorno
        else:
            if not retorno["continue"]:
                result["expTipo"] = retorno["expTipo"]
                result["expValor"] = retorno["expValor"]
                return result["expTipo"]
            else:
                return result
        return

    def getValor(self, driver, ts):
        result = {"return":False, "break":False, "continue":False, "expTipo":"", "expValor": ""}
        if result["expTipo"] != "":
            return result["expValor"]
        return self.code[(len(self.code)-1)].getValor(driver, ts)