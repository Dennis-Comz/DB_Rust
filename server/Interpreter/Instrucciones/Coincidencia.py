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

    def ejecutar(self, driver: Driver, ts: TablaSimbolos, errores):
        result = {"return":False, "break":False, "continue":False, "expTipo":"", "expValor": ""}

        try:
            if getattr(self.cuerpo, "ejecutar", None) != None:
                retorno = self.cuerpo.ejecutar(driver, ts, errores)
                if retorno != None:
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
        except Exception as d:
            if type(d.args[0]) == dict:
                errores.append(d.args[0])
            pass
    
    def getTipo(self, driver, ts, errores):
        result = {"return":False, "break":False, "continue":False, "expTipo":"", "expValor": ""}

        if getattr(self.cuerpo, "getTipo", None) != None:
            return self.cuerpo.getTipo(driver, ts, errores)

        retorno = self.ejecutar(driver, ts, errores)
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

    def getValor(self, driver, ts, errores):
        result = {"return":False, "break":False, "continue":False, "expTipo":"", "expValor": ""}
        if result["expTipo"] != "":
            return result["expValor"]
        return self.cuerpo.getValor(driver, ts, errores)


    def getValores(self, driver, ts, errores):
        vals = []
        
        if self.valores != []:
            for val in self.valores:
                vals.append(val.getValor(driver, ts, errores))
        
        return vals

    def getTipos(self, driver, ts, errores):
        types = []
        if self.valores != []:
            for val in self.valores:
                types.append(val.getTipo(driver, ts, errores))
        
        return types