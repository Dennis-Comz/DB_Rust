from Analizador import lexer
from plyFiles.ply.yacc import yacc
from Interpreter.AST.ast import Ast
from Interpreter.Instrucciones.Print import Print
from Interpreter.TablaSimbolos.Tipos import Tipos
from Interpreter.Expresiones.ToOwned import ToOwned
from Interpreter.Expresiones.ToString import ToString
from Interpreter.Expresiones.Primitivo import Primitivo
from Interpreter.Instrucciones.Declaracion import Declaracion
from Interpreter.Expresiones.Identificador import Identificador
from Interpreter.Expresiones.Operaciones.Logicas import Logicas
from Interpreter.TablaSimbolos.Simbolo import Simbolo, Simbolos
from Interpreter.Expresiones.Operaciones.Aritmeticas import Aritmeticas
from Interpreter.Expresiones.Operaciones.Relacionales import Relacionales

tokens = lexer.tokens

# PRECEDENCIA
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('right', 'NOT'),
    ('left', 'IGUAL_IGUAL', 'NO_IGUAL', 'MENOR', 'MAYOR', 'MENOR_IGUAL', 'MAYOR_IGUAL'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'MULTI', 'DIV', 'MODULO'),
    ('right', 'UNARIO')
)

# DEFINICION INICIO GRAMATICA
# inicio : instrucciones
# instrucciones: instrucciones instruccion PT_COMA
#            | instruccion PT_COMA
# instruccion : PRINT PARA expresion PARC
#           | declaracion
# declaracion : LET MUT ID DOS_PT tipo IGUAL expresion
#           | LET MUT ID DOS_PT tipo
#           | LET MUT ID IGUAL expresion
#           | LET MUT ID
#           | LET ID DOS_PT tipo IGUAL expresion
#           | LET ID DOS_PT tipo
#           | LET ID IGUAL expresion
#           | LET ID
#           | ID IGUAL expresion
# expresion : expresion MAS expresion
#           | expresion MENOS expresion
#           | expresion MULTI expresion
#           | expresion DIV expresion
#           | expresion MODULO expresion
#           | I64 DOS_PT DOS_PT POW PARA expresion COMA expresion PARC
#           | expresion IGUAL_IGUAL expresion
#           | expresion NO_IGUAL expresion
#           | expresion MAYOR expresion
#           | expresion MENOR expresion
#           | expresion MAYOR_IGUAL expresion
#           | expresion MENOR_IGUAL expresion
#           | PARA expresion PARC
#           | MENOS expresion
#           | expresion AND expresion
#           | expresion OR expresion
#           | NOT expresion
#           | expresion TO_OWNED PARA PARC
#           | expresion TO_STRING PARA PARC
#           | CADENA
#           | CARACTER
#           | TRUE
#           | FALSE
#           | ENTERO
#           | DECIMAL
#           | ID

def p_inicio(p):
    """
    inicio : instrucciones
    """
    p[0] = Ast(p[1])

def p_lista_instrucciones(p):
    """
    instrucciones : instrucciones instruccion PT_COMA
    """
    p[1].append(p[2])
    p[0] = p[1]

def p_instrucciones_instruccion(p):
    """
    instrucciones : instruccion PT_COMA
    """ 
    p[0] = [p[1]]

def p_instruccion(p):
    """
    instruccion : print
                | declaracion
    """
    p[0] = p[1]

def p_instruccion_print(p):
    """
    print : PRINT PARA expresion PARC
    """
    p[0] = Print(p[3], p.lineno(1), 0)

def p_instruccion_declaracion(p):
    """
    declaracion : LET MUT ID DOS_PT tipo IGUAL expresion
    """
    p[0] = Declaracion(
        True,
        p[3],
        Simbolo(Simbolos.VARIABLE, True, p[5], p[3], p[7]),
        p[5],
        p.lineno(1),
        p.lexpos(5)
    )

def p_declaracion_2(p):
    """
    declaracion : LET MUT ID DOS_PT tipo
    """
    p[0] = Declaracion(
        True,
        p[3],
        Simbolo(Simbolos.VARIABLE, True, p[3], p[5], None),
        p[5],
        p.lineno(1),
        0
    )

def p_declaracion_3(p):
    """
    declaracion : LET MUT ID IGUAL expresion
    """
    p[0] = Declaracion(
        True,
        p[3],
        Simbolo(Simbolos.VARIABLE, True, p[3], None, p[5]),
        None,
        p.lineno(1),
        0
    )

def p_declaracion_4(p):
    """
    declaracion : LET MUT ID
    """
    p[0] = Declaracion(
        True,
        p[3],
        Simbolo(Simbolos.VARIABLE, True, p[3], None, None),
        None,
        p.lineno(1),
        0
    )

def p_declaracion_5(p):
    """
    declaracion : LET ID DOS_PT tipo IGUAL expresion
    """
    p[0] = Declaracion(
        False,
        p[2],
        Simbolo(Simbolos.VARIABLE, False, p[2], p[4], p[6]),
        p[4],
        p.lineno(1),
        0
    )

def p_declaracion_6(p):
    """
    declaracion : LET ID DOS_PT tipo
    """
    p[0] = Declaracion(
        False,
        p[2],
        Simbolo(Simbolos.VARIABLE, False, p[2], p[4], None),
        p[4],
        p.lineno(1),
        0
    )

def p_declaracion_7(p):
    """
    declaracion : LET ID IGUAL expresion
    """
    p[0] = Declaracion(
        False,
        p[2],
        Simbolo(Simbolos.VARIABLE, False, p[2], None, p[4]),
        None,
        p.lineno(1),
        0
    )

def p_declaracion_8(p):
    """
    declaracion : LET ID
    """
    p[0] = Declaracion(
        False,
        p[2],
        Simbolo(Simbolos.VARIABLE, False, p[2], None, None),
        None,
        p.lineno(1),
        0
    )

def p__declaracion_asignacion(p):
    """
    declaracion : ID IGUAL expresion
    """
    p[0] = Declaracion(
        False,
        p[1],
        Simbolo(Simbolos.VARIABLE, False, p[1], None, p[3]),
        None,
        p.lineno(1),
        p.lexpos(1)
    )
# === FIN DIFERENTES DECLARACIONES ===

def p_tipo(p):
    """
    tipo : I64
        | F64
        | BOOL
        | STRING
        | STR
    """
    if p[1] == 'i64':
        p[0] = Tipos.INT64
    elif p[1] == 'f64':
        p[0] = Tipos.FLOAT64
    elif p[1] == 'bool':
        p[0] = Tipos.BOOLEAN
    elif p[1] == 'String':
        p[0] = Tipos.STR_BUFFER
    elif p[1] == '&str':
        p[0] = Tipos.STR_POINTER

# === INICIO ARITMETICAS
def p_exp_aritmeticas(p):
    """
    expresion : expresion MAS expresion
           | expresion MENOS expresion
           | expresion MULTI expresion
           | expresion DIV expresion
           | expresion MODULO expresion
    """
    p[0] = Aritmeticas(exp1 = p[1], operador = p[2], exp2 = p[3], expU = False, linea = p.lineno(1), columna = p.lexpos)

def p_exp_potencia(p):
    """
    expresion : I64 DOS_PT DOS_PT POW PARA expresion COMA expresion PARC
    """
    p[0] = Aritmeticas(exp1 = p[6], operador = '^', exp2 = p[8], expU = False, linea = p.lineno(1), columna = p.lexpos)

def p_exp_parentesis(p):
    """
    expresion : PARA expresion PARC
    """
    p[0] = p[2]


def p_exp_unario(p):
    """
    expresion : MENOS expresion %prec UNARIO
    """
    p[0] = Aritmeticas(exp1=p[2], operador='UNARIO', exp2=None, expU=True, linea=p.lineno(1), columna = p.lexpos)

# === FIN ARITMETICAS ===

# === INICIO RELACIONALES ===
def p_exp_relacionales(p):
    """
    expresion : expresion IGUAL_IGUAL expresion
            | expresion NO_IGUAL expresion
            | expresion MAYOR expresion
            | expresion MENOR expresion
            | expresion MAYOR_IGUAL expresion
            | expresion MENOR_IGUAL expresion
    """
    p[0] = Relacionales(exp1 = p[1], operador = p[2], exp2 = p[3], linea = p.lineno(1), columna = p.lexpos)
# === FIN RELACIONALES ===

# === INICIO LOGICAS ===
def p_exp_logicas(p):
    """
    expresion : expresion AND expresion
            | expresion OR expresion
    """
    p[0] = Logicas(exp1 = p[1], operador = p[2], exp2 = p[3], linea = p.lineno(1), columna = p.lexpos(1))

def p_exp_not(p):
    """
    expresion : NOT expresion
    """
    p[0] = Logicas(exp1 = None, operador = p[1], exp2 = p[2], linea = p.lineno(1), columna = p.lexpos(1))

# === FIN LOGICAS ===

def p_exp_cadena_toowned(p):
    """
    expresion : expresion PUNTO TO_OWNED PARA PARC
    """
    p[0] = ToOwned(p[1], Tipos.STR_BUFFER, p.lineno(1), 0)

def p_exp_cadena_tostring(p):
    """
    expresion : expresion PUNTO TO_STRING PARA PARC
    """
    p[0] = ToString(p[1], Tipos.STR_BUFFER, p.lineno(1), 0)

# === INICIO TIPOS DE DATO ===
def p_exp_entero(p):
    """
    expresion :  ENTERO
    """
    p[0] = Primitivo(p[1], Tipos.INT64, p.lineno(1), 0)

def p_exp_decimal(p):
    """
    expresion : DECIMAL
    """
    p[0] = Primitivo(p[1], Tipos.FLOAT64, p.lineno(1), 0)

def p_exp_caracter(p):
    """
    expresion : CARACTER
    """
    p[0] = Primitivo(p[1], Tipos.CARACTER, p.lineno(1), 0)

def p_exp_cadena_pointer(p):
    """
    expresion : CADENA
    """
    p[0] = Primitivo(p[1], Tipos.STR_POINTER, p.lineno(1), 0)
    
def p_exp_booleano(p):
    """
    expresion : TRUE
            | FALSE
    """
    if p[1] == 'true':
        p[0] = Primitivo(True, Tipos.BOOLEAN, p.lineno(1), 0)
    elif p[1] == 'false':
        p[0] = Primitivo(False, Tipos.BOOLEAN, p.lineno(1), 0)

def p_exp_identificador(p):
    """
    expresion : ID
    """
    p[0] = Identificador(p[1], p.lineno(1), 0)


# === FIN TIPOS DE DATO ===

# Error sintactico
def p_error(p):
    print(f'Error de sintaxis {p.value!r} en la linea {p.lineno} columna {p.lexpos}')

# Build the parser
parser = yacc(debug=True)