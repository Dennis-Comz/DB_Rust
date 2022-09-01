from Interpreter.Expresiones.Expresion import Expresion
from Interpreter.Instrucciones.Instruccion import Instruccion
from Interpreter.TablaSimbolos.TablaSimbolos import TablaSimbolos
from Interpreter.Driver.Driver import Driver
from Interpreter.TablaSimbolos.Tipos import Tipos
from Interpreter.TablaSimbolos.Simbolo import Simbolo, Simbolos

class LlamadaFuncion(Instruccion, Expresion):
    def __init__(self, id:str, parametros, linea:int, columna: int):
        self.id = id
        self.parametros = parametros
        self.linea = linea
        self.columna = columna
        self.salida = {"tipo": None, "valor":""}

    def ejecutar(self, driver: Driver, ts: TablaSimbolos):
        try:
            funcion = ts.buscarFuncion(self.id)
            
            if funcion != None:
                if len(self.parametros) == len(funcion.parametros):
                    ts_local = TablaSimbolos(ts, "FUNCION")
                    for i in range(0, len(self.parametros)):
                        tipoParam = self.parametros[i].getTipo(driver, ts)
                        if tipoParam != funcion.parametros[i].type:
                            driver.append(f'Error Semantico, se esperaba parametro {funcion.parametros[i].type} se obtuvo {tipoParam}, linea {self.linea}, columna {self.columna}')
                            raise Exception(f'Error Semantico, se esperaba parametro {funcion.parametros[i].type} se obtuvo {tipoParam}, linea {self.linea}, columna {self.columna}')
                    for i in range(0, len(self.parametros)):
                        valorParam = self.parametros[i].getValor(driver, ts)
                        ts_local.add(funcion.parametros[i].id, Simbolo(
                            Simbolos.VARIABLE, True, funcion.parametros[i].id, 
                            funcion.parametros[i].type, valorParam))
                    if funcion.tipo == Tipos.VOID:
                        return funcion.cuerpo.ejecutar(driver, ts_local)
                    else:
                        result = funcion.cuerpo.ejecutar(driver, ts_local)
                        if result != None and result["return"]:
                            tipoExp = result["expTipo"]
                            valExp = result["expValor"]
                            if tipoExp == funcion.tipo:
                                return {"tipo": tipoExp, "valor":valExp}
                            else:
                                driver.append(f'Error Semantico, se esperaba tipo de retorno {funcion.tipo} se obtuvo {tipoExp}, linea {self.linea}, columna {self.columna}')
                                raise Exception(f'Error Semantico, se esperaba tipo de retorno {funcion.tipo} se obtuvo {tipoExp}, linea {self.linea}, columna {self.columna}')
        except:
            pass

    def getTipo(self, driver, ts):
        tipo = self.ejecutar(driver, ts)
        if tipo != None:
            if self.salida["tipo"] != None:
                self.salida["tipo"] = tipo["tipo"]
                self.salida["valor"] = tipo["valor"]
                return self.salida["tipo"]
            else:
                self.salida = tipo
                return self.salida["tipo"]
        driver.append(f'Error Semantico, la variable no tiene retorno, linea {self.linea}, columna {self.columna}')
        raise Exception(f'Error Semantico, la variable no tiene retorno, linea {self.linea}, columna {self.columna}')

    def getValor(self, driver, ts):
        if self.salida["valor"] is not None:
            return self.salida["valor"]