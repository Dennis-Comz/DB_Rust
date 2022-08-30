from Interpreter.TablaSimbolos.Tipos import Tipos

class Parametro:
    def __init__(self, type:Tipos, id:str):
        self.type = type
        self.id = id