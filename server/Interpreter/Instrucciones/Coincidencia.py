from Interpreter.Expresiones.Expresion import Expresion
from Interpreter.Instrucciones.Instruccion import Instruccion
from Interpreter.TablaSimbolos.TablaSimbolos import TablaSimbolos
from Interpreter.TablaSimbolos.Tipos import Tipos
from Interpreter.Driver.Driver import Driver

class Coincidencia(Instruccion, Expresion):
    def __init__(self, valores, cuerpo, linea: int, columna: int):
        self.valores = valores
        self.cuerpo = cuerpo
        self.linea = linea
        self.columna = columna
        self.result = {"return":False, "break":False, "continue":False, "expTipo":"", "expValor": ""}

    def ejecutar(self, driver: Driver, ts: TablaSimbolos):
        result = {"return":False, "break":False, "continue":False, "expTipo":"", "expValor": ""}

        if getattr(self.cuerpo, "ejecutar", None) != None:
            retorno = self.cuerpo.ejecutar(driver, ts)
            if retorno != None:
                result["expTipo"] = retorno["expTipo"]
                result["expValor"] = result["expValor"] + retorno["expValor"]
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
        if getattr(self.cuerpo, "getTipo", None) != None:
            return self.cuerpo.getTipo(driver, ts)
        retorno = self.cuerpo.ejecutar(driver, ts)
        if self.result["expTipo"] == "":
            self.result = retorno
        else:
            if not retorno["continue"]:
                self.result["expTipo"] = retorno["expTipo"]
                self.result["expValor"] = retorno["expValor"]
                return self.result["expTipo"]
            else:
                return self.result
        return self.result["expTipo"]

            # if retorno != None:
            #     self.result["expRetorno"] = retorno["expRetorno"]
            # if retorno["break"]:
            #     self.result["break"] = True
            #     return self.result["expRetorno"].getTipo(driver, ts)
            # elif retorno["continue"]:
            #     self.result["continue"] = True
            #     return self.result
            # elif retorno["return"]:
            #     self.result["return"] = True
            #     return self.result["expRetorno"].getTipo(driver, ts)
            

    def getValor(self, driver, ts):
        if self.result["expTipo"] != "":
            return self.result["expValor"]
        # if getattr(self.cuerpo, "ejecutar", None) != None:
        #     return self.result["valor"]
        return self.cuerpo.getValor(driver, ts)


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