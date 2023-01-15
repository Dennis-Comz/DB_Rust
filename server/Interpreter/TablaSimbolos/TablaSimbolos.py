from Interpreter.TablaSimbolos.Simbolo import Simbolo
from Interpreter.TablaSimbolos.Funcion import Funcion
from Interpreter.TablaSimbolos.Arreglo import Arreglo

class TablaSimbolos:

    def __init__(self, anterior, env):
        self.env = env
        self.anterior = anterior
        self.tabla = {}
        self.tablaFunciones = {}
        self.tablaArreglos = {}

#    ====    METODOS PARA VARIABLES     ====
    def add(self, id: str, simbolo: Simbolo):
        self.tabla[id] = simbolo

    def buscar(self, id: str) -> Simbolo:
        ts = self

        while ts is not None:
            exist = ts.tabla.get(id)

            if exist is not None:
                return exist

            ts = ts.anterior

        return None

    def buscarActual(self, id: str) -> Simbolo:
        return self.tabla.get(id)

    def eliminar_variable(self, id:str):
        ts = self
        while ts is not None:
            exist = ts.tabla.get(id)

            if exist is not None:
                del ts.tabla[id]
                return True

            ts = ts.anterior

        return False

#  ====     FIN METODOS VARIABLES   =====

# ==== INICIO METODOS FUNCIONES ====
    def addFuncion(self, id:str, simbolo:Funcion):
        self.tablaFunciones[id] = simbolo

    def buscarFuncion(self, id:str) -> Funcion:
        ts = self
        while ts is not None:
            exist = ts.tablaFunciones.get(id)
            if exist is not None:
                return exist
            ts = ts.anterior
        return None

    def buscarFuncionActual(self, id:str) -> Funcion:
        return self.tablaFunciones.get(id) 

#  ====    FIN METODOS FUNCIONES   =====

# ==== INICIO METODOS ARREGLOS ====
    def addArreglo(self, id:str, simbolo:Arreglo):
        self.tablaArreglos[id] = simbolo

    def buscarArreglo(self, id:str) -> Arreglo:
        ts = self
        while ts is not None:
            exist = ts.tablaArreglos.get(id)
            if exist is not None:
                return exist
            ts = ts.anterior
        return None

    def buscarArregloActual(self, id:str) -> Arreglo:
        return self.tablaArreglos.get(id) 

#  ====    FIN METODOS FUNCIONES   =====