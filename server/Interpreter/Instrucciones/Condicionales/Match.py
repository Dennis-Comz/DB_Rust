from Interpreter.Expresiones.Expresion import Expresion
from Interpreter.Instrucciones.Instruccion import Instruccion
from Interpreter.TablaSimbolos.TablaSimbolos import TablaSimbolos
from Interpreter.TablaSimbolos.Tipos import Tipos
from Interpreter.Driver.Driver import Driver
from Interpreter.Instrucciones.Coincidencia import Coincidencia
from static import simbs

class Match(Instruccion, Expresion):
    def __init__(self, valor:Expresion, coincidencias, linea: int, columna: int):
        self.valor = valor
        self.coincidencias = coincidencias
        self.linea = linea
        self.columna = columna

    def ejecutar(self, driver: Driver, ts: TablaSimbolos, errores):
        try:
            ts_local = TablaSimbolos(ts, 'MATCH')
            expTipo = self.valor.getTipo(driver, ts, errores)
            expValor = self.valor.getValor(driver, ts, errores)

            salir = True
            for coin in self.coincidencias:
                tipos = coin.getTipos(driver, ts_local, errores)
                valores = coin.getValores(driver, ts_local, errores)
                for i in range(0, len(valores)):
                    if expValor == valores[i] and expTipo == tipos[i]:
                        retorno = coin.ejecutar(driver, ts_local, errores)
                        if retorno != None:
                            simbs.append(ts_local)
                            return retorno
                        salir = False
                        break
                    elif expTipo != tipos[i]:
                        driver.append(f'Error Semantico, no se puede comparar {expTipo} con {tipos[i]}, linea {self.valor.linea}, columna {self.valor.columna}')
                        raise Exception({"tipo":"Semantico", "descripcion":f"no se puede comparar {expTipo} con {tipos[i]}", "linea": str(self.valor.linea), "columna":str(self.valor.columna), "ambito": ts_local.env})
                if len(valores) == 0:
                    retorno = coin.ejecutar(driver, ts_local, errores)
                    if retorno != None:
                        simbs.append(ts_local)
                        return retorno
                    salir = False
                if not salir:
                    break
            simbs.append(ts_local)
            
        except Exception as d:
            if type(d.args[0]) == dict:
                errores.append(d.args[0])
            pass

    def getTipo(self, driver, ts):
        ts_local = TablaSimbolos(ts, 'MATCH')
        expTipo = self.valor.getTipo(driver, ts)
        expValor = self.valor.getValor(driver, ts)

        salir = True
        for coin in self.coincidencias:
            valores = coin.getValores(driver, ts_local)
            tipos = coin.getTipos(driver, ts_local)
            for i in range(0, len(valores)):
                if expValor == valores[i] and expTipo == tipos[i]:
                    return coin.getTipo(driver, ts_local)
                elif expTipo != tipos[i]:
                    driver.append(f'Error Semantico, no se puede comparar {expTipo} con {tipos[i]}, linea {self.valor.linea}, columna {self.valor.columna}')
                    raise Exception({"tipo":"Semantico", "descripcion":f"no se puede comparar {expTipo} con {tipos[i]}", "linea": str(self.valor.linea), "columna":str(self.valor.columna)})
            if len(valores) == 0:
                return coin.getTipo(driver, ts_local)
            if not salir:
                break

    def getValor(self, driver, ts):
        ts_local = TablaSimbolos(ts, 'MATCH')
        expTipo = self.valor.getTipo(driver, ts)
        expValor = self.valor.getValor(driver, ts)

        salir = True
        for coin in self.coincidencias:
            valores = coin.getValores(driver, ts_local)
            tipos = coin.getTipos(driver, ts_local)
            for i in range(0, len(valores)):
                if expValor == valores[i] and expTipo == tipos[i]:
                    return coin.getValor(driver, ts_local)
                elif expTipo != tipos[i]:
                    driver.append(f'Error Semantico, no se puede comparar {expTipo} con {tipos[i]}, linea {self.valor.linea}, columna {self.valor.columna}')
                    raise Exception({"tipo":"Semantico", "descripcion":f"no se puede comparar {expTipo} con {tipos[i]}", "linea": str(self.valor.linea), "columna":str(self.valor.columna)})
            if len(valores) == 0:
                return coin.getValor(driver, ts_local)
            if not salir:
                break
        