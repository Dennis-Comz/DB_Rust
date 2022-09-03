from Interpreter.Instrucciones.Metodo import Metodo
from Interpreter.Expresiones.LlamadaFuncion import LlamadaFuncion


class Ast:

    def __init__(self, instrucciones=None):
        if instrucciones is None:
            instrucciones = []
        self.instrucciones = instrucciones

    def ejecutar(self, driver, ts, errores):
        lineaMain = 0
        columnaMain = 0
        for instruccion in self.instrucciones:
            if isinstance(instruccion, Metodo):
                if instruccion.nombre == "main":
                    lineaMain = instruccion.linea
                    columnaMain = instruccion.columna
                instruccion.ejecutar(driver, ts, errores)
        main = ts.buscarFuncion("main")
        if main is not None:
            LlamadaFuncion(main.nombre, main.parametros, lineaMain, columnaMain).ejecutar(driver, ts, errores)
            print()

