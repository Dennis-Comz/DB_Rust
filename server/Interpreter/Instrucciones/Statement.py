import traceback
from Interpreter.Expresiones.Expresion import Expresion
from Interpreter.Instrucciones.Instruccion import Instruccion
from Interpreter.TablaSimbolos.TablaSimbolos import TablaSimbolos
from Interpreter.Driver.Driver import Driver

class Statement(Instruccion, Expresion):
    array = []
    result = {"return":False, "break":False, "continue":False, "expTipo":"", "expValor": ""}

    def __init__(self, code, linea: int, columna: int):
        self.code = code
        self.linea = linea
        self.columna = columna
        #self.result = {"return":False, "break":False, "continue":False, "expTipo":"", "expValor": ""}

    def ejecutar(self, driver: Driver, ts: TablaSimbolos):
        
        for ins in self.code:
            retorno = ins.ejecutar(driver, ts)
            if retorno is not None:
                self.result["expTipo"] = retorno["expTipo"]
                if len(self.array) == 0:
                    self.array.append(retorno["expValor"])
                else:
                    self.array.append(self.array[len(self.array)-1] + retorno["expValor"])
                self.result["expValor"] = self.array[len(self.array)-1]
                if retorno["break"]:
                    self.result["break"] = True
                    return self.result
                elif retorno["continue"]:
                    self.result["continue"] = True
                    return self.result
                elif retorno["return"]:
                    self.result["return"] = True
                    return self.result


    def getTipo(self, driver, ts):
        if getattr(self.code[(len(self.code)-1)], "getTipo", None) != None:
            return self.code[(len(self.code)-1)].getTipo(driver, ts)
        retorno = self.ejecutar(driver, ts)
        if self.result["expTipo"] == "":
            self.result = retorno
        else:
            if not retorno["continue"]:
                self.result["expTipo"] = retorno["expTipo"]
                self.result["expValor"] = retorno["expValor"]
                return self.result["expTipo"]
            else:
                return self.result
        return
        # for ins in self.code:
        #     if getattr(ins, "ejecutar", None) != None:
        #         retorno = ins.ejecutar(driver, ts)
        #         if retorno != None:
        #             self.result1["expRetorno"] = retorno["expRetorno"]
        #             if retorno["break"]:
        #                 self.result1["break"] = True
        #                 return self.result1["expRetorno"].getTipo(driver, ts)
        #             elif retorno["continue"]:
        #                 self.result1["continue"] = True
        #                 return self.result1
        #             elif retorno["return"]:
        #                 self.result1["return"] = True
        #                 return self.result1["expRetorno"].getTipo(driver, ts)

    def getValor(self, driver, ts):
        if self.result["expTipo"] != "":
            return self.result["expValor"]
        return self.code[(len(self.code)-1)].getValor(driver, ts)