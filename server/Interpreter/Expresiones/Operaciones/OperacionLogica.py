from enum import Enum
from Interpreter.Expresiones.Expresion import Expresion

class Operador(Enum):
    AND = 1
    OR = 2
    NOT = 3

def getOperador(op) -> Operador:
    if op == '&&':
        return Operador.AND
    elif op == '||':
        return Operador.OR
    elif op == '!':
        return Operador.NOT
    
def getOperacion(op: Operador):
    if op == Operador.AND:
        return lambda val1, val2: val1 and val2
    elif op == Operador.OR:
        return lambda val1, val2: val1 or val2
    elif op == Operador.NOT:
        return lambda val2:  not val2

class OperacionLogica(Expresion):

    def __init__(self, exp1, operador, exp2: Expresion, linea, columna):
        super().__init__()
        self.columna = columna
        self.linea = linea
        self.exp2 = exp2
        self.operador = getOperador(operador)
        self.exp1 = exp1