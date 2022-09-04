from Interpreter.Instrucciones.Instruccion import Instruccion
from Interpreter.Driver.Driver import Driver
from Interpreter.TablaSimbolos.TablaSimbolos import TablaSimbolos
from Interpreter.TablaSimbolos.Funcion import Funcion

class Metodo(Instruccion):
                            #Array de objetos tipo parametro
                                        # |
    def __init__(self, nombre:str, parametros, tipo, cuerpo:Instruccion, simbolo: Funcion, linea:int, columna:int):
        self.nombre = nombre
        self.parametros = parametros
        self.tipo = tipo
        self.cuerpo = cuerpo
        self.simbolo = simbolo
        self.linea = linea
        self.columna = columna
    
    def ejecutar(self, driver: Driver, ts: TablaSimbolos, errores):
        try:
            existe = ts.buscarFuncion(self.nombre)
            if existe is None:
                ts.addFuncion(self.nombre, self.simbolo)
            else:
                driver.append(f'Error semantico, la funcion {self.nombre} ya ha sido declarada, linea {self.linea}, columna {self.columna}')
                raise Exception({"tipo":"Semantico", "descripcion":f"la funcion {self.nombre} ya ha sido declarada", "linea": str(self.linea), "columna":str(self.columna), "ambito": ts.env})
        except Exception as d:
            if type(d.args[0]) == dict:
                errores.append(d.args[0])
            pass
