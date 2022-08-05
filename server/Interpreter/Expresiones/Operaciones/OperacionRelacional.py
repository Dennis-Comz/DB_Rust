from enum import Enum
from Interpreter.Expresiones.Expresion import Expresion

class Operador(Enum):
    IGUAL_IGUAL = 1
    NO_IGUAL = 2
    MAYOR = 3
    MENOR = 4
    MAYOR_IGUAL = 5
    MENOR_IGUAL = 6

def getOperador(op) -> Operador:
    if op == '==':
        return Operador.IGUAL_IGUAL
    elif op == '!=':
        return Operador.NO_IGUAL
    elif op == '>':
        return Operador.MAYOR
    elif op == '<':
        return Operador.MENOR
    elif op == '>=':
        return Operador.MAYOR_IGUAL
    elif op == '<=':
        return Operador.MENOR_IGUAL

def getOperacion(op: Operador):
    if op == Operador.IGUAL_IGUAL:
        return lambda val1, val2: val1 == val2
    elif op == Operador.NO_IGUAL:
        return lambda val1, val2: val1 != val2
    elif op == Operador.MAYOR:
        return lambda val1, val2: val1 > val2
    elif op == Operador.MENOR:
        return lambda val1, val2: val1 < val2
    elif op == Operador.MAYOR_IGUAL:
        return lambda val1, val2: val1 >= val2
    elif op == Operador.MENOR_IGUAL:
        return lambda val1, val2: val1 <= val2

class OperacionRelacional(Expresion):

    def __init__(self, exp1: Expresion, operador, exp2: Expresion, linea, columna):
        super().__init__()
        self.columna = columna
        self.linea = linea
        self.exp2 = exp2
        self.operador = getOperador(operador)
        self.exp1 = exp1