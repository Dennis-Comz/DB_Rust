from Interpreter.TablaSimbolos.Simbolo import Simbolo
from Interpreter.TablaSimbolos.Funcion import Funcion

class TablaSimbolos:

    def __init__(self, anterior, env):
        self.env = env
        self.anterior = anterior
        self.tabla = {}
        self.tablaFunciones = {}
        self.tablaClases = {}

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

#  ====     FIN METODOS VARIABLES   =====

# ==== INICIO METODOS FUNCIONES ====
    def addFuncion(self, id:str, simbolo:Funcion):
        self.tablaFunciones[id] = simbolo

    def buscarFuncion(self, id:str) -> Funcion:
        tsFunc = self
        while tsFunc is not None:
            exist = tsFunc.tablaFunciones.get(id)
            if exist is not None:
                return exist
            tsFunc = tsFunc.anterior
        return None

    def buscarFuncionActual(self, id:str) -> Funcion:
        return self.tablaFunciones.get(id) 

#  ====    FIN METODOS FUNCIONES   =====