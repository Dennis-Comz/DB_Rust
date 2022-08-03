from plyFiles.ply.yacc import yacc
from Analizador import lexer
from Interpreter.Instrucciones.Print import Print
from Interpreter.Expresiones.Operaciones.Aritmeticas import Aritmeticas
from Interpreter.Expresiones.Primitivo import Primitivo
from Interpreter.AST.ast import Ast

tokens = lexer.tokens

# PRECEDENCIA
precedence = (
    ('left', 'MAS', 'MENOS'),
    ('left', 'MULTI', 'DIV', 'MODULO'),
    ('right', 'POTENCIA'),
    ('right', 'UNARIO')
)

# DEFINICION INICIO GRAMATICA
# inicio : instrucciones
# instrucciones: instrucciones instruccion PT_COMA
#            | instruccion PT_COMA
# instruccion : PRINT PARA expresion PARC
# expresion : expresion MAS expresion
#           | expresion MENOS expresion
#           | expresion MULTI expresion
#           | expresion DIV expresion
#           | expresion MODULO expresion
#           | expresion POTENCIA expresion
#           | PARA expresion PARC
#           | MENOS expresion
#           | ENTERO
#           | DECIMAL

def p_inicio(p):
    """
    inicio : instrucciones
    """
    p[0] = Ast(p[1])

def p_lista_instrucciones(p):
    """
    instrucciones : instrucciones instruccion PT_COMA
    """
    p[0] = p[1].append(p[2])

def p_instrucciones_instruccion(p):
    """
    instrucciones : instruccion PT_COMA
    """ 
    p[0] = [p[1]]

def p_instruccion_print(p):
    """
    instruccion : PRINT PARA expresion PARC
    """
    p[0] = Print(p[3], p.lineno(1), 0)

def p_exp_aritmeticas(p):
    """
    expresion : expresion MAS expresion
           | expresion MENOS expresion
           | expresion MULTI expresion
           | expresion DIV expresion
           | expresion MODULO expresion
           | expresion POTENCIA expresion
    """
    p[0] = Aritmeticas(exp1 = p[1], operador = p[2], exp2 = p[3], expU = False, linea = p.lineno(1), columna = 0)

def p_exp_parentesis(p):
    """
    expresion : PARA expresion PARC
    """
    p[0] = p[2]


def p_exp_unario(p):
    """
    expresion : MENOS expresion %prec UNARIO
    """
    p[0] = Aritmeticas(exp1=p[2], operador='UNARIO', exp2=None, expU=True, linea=p.lineno(1), columna=0)


def p_exp_numero(p):
    """
    expresion :  ENTERO
              | DECIMAL
    """
    p[0] = Primitivo(p[1], p.lineno(1), 0)


# Error sintactico
def p_error(p):
    print(f'Error de sintaxis {p.value!r}')


# Build the parser
parser = yacc()