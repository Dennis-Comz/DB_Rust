from enum import Enum
from Interpreter.Expresiones.Expresion import Expresion


class Operador(Enum):
    SUMA = 1
    RESTA = 2
    MULTI = 3
    DIV = 4
    POTENCIA = 5
    MODULO = 6
    UNARIO = 7


def getOperador(op) -> Operador:
    if op == '+':
        return Operador.SUMA
    elif op == '-':
        return Operador.RESTA
    elif op == '*':
        return Operador.MULTI
    elif op == '/':
        return Operador.DIV
    elif op == '^':
        return Operador.POTENCIA
    elif op == '%':
        return Operador.MODULO
    elif op == 'UNARIO':
        return Operador.UNARIO


def getOperacion(op: Operador):
    if op == Operador.SUMA:
        return lambda num1, num2: num1 + num2
    elif op == Operador.RESTA:
        return lambda num1, num2: num1 - num2
    elif op == Operador.MULTI:
        return lambda num1, num2: num1 * num2
    elif op == Operador.DIV:
        return lambda num1, num2: num1 / num2
    elif op == Operador.POTENCIA:
        return lambda num1, num2: num1 ** num2
    elif op == Operador.MODULO:
        return lambda num1, num2: num1 % num2


class Operacion(Expresion):

    def __init__(self, exp1: Expresion, operador, exp2: Expresion, linea, columna, expU):
        super().__init__()
        self.expU = expU
        self.columna = columna
        self.linea = linea
        self.exp2 = exp2
        self.operador = getOperador(operador)
        self.exp1 = exp1