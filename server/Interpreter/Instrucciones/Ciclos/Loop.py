from Interpreter.Expresiones.Expresion import Expresion
from Interpreter.Instrucciones.Instruccion import Instruccion
from Interpreter.TablaSimbolos.TablaSimbolos import TablaSimbolos
from Interpreter.Driver.Driver import Driver

class Loop(Instruccion, Expresion):
    def __init__(self, cuerpo, linea, columna):
        self.cuerpo = cuerpo
        self.linea = linea
        self.columna = columna

    def ejecutar(self, driver: Driver, ts: TablaSimbolos, errores):
        try:
            ts_local = TablaSimbolos(ts, 'LOOP')
            while True:
                retorno = self.cuerpo.ejecutar(driver, ts_local, errores)
                if retorno != None:
                    if retorno["continue"]:
                        continue;
                    else:
                        return retorno
        except Exception as d:
            if type(d.args[0]) == dict:
                errores.append(d.args[0])
            pass

    def getTipo(self, driver, ts, errores):
        ts_local = TablaSimbolos(ts, 'LOOP')
        while True:
            tipo = self.cuerpo.getTipo(driver, ts_local, errores)
            if tipo != None:
                if type(tipo) == dict and tipo["continue"]:
                        continue;
                else:
                    return tipo

    def getValor(self, driver, ts, errores):
        ts_local = TablaSimbolos(ts, 'LOOP')
        while True:
            valor = self.cuerpo.getValor(driver, ts_local, errores)
            if valor != None:
                if type(valor) == dict and valor["continue"]:
                        continue;
                else:
                    return valor
