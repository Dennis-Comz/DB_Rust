from Interpreter.TablaSimbolos.Tipos import Tipos

class Parametro:
    def __init__(self, type:Tipos, id:str, isArray:bool, mutable:bool):
        self.type = type
        self.id = id
        self.isArray = isArray
        self.mutable = mutable