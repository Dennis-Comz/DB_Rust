from Analizador import lexer
from plyFiles.ply.yacc import yacc
from Interpreter.AST.ast import Ast
from Interpreter.Expresiones.Raiz import Raiz
from Interpreter.Expresiones.Casteo import Casteo
from Interpreter.TablaSimbolos.Tipos import Tipos
from Interpreter.Expresiones.ToOwned import ToOwned
from Interpreter.Expresiones.Absoluto import Absoluto
from Interpreter.Instrucciones.PrintLn import PrintLn
from Interpreter.Expresiones.ToString import ToString
from Interpreter.Expresiones.Primitivo import Primitivo
from Interpreter.Instrucciones.Statement import Statement
from Interpreter.Instrucciones.Declaracion import Declaracion
from Interpreter.Expresiones.Identificador import Identificador
from Interpreter.Expresiones.Operaciones.Logicas import Logicas
from Interpreter.TablaSimbolos.Simbolo import Simbolo, Simbolos
from Interpreter.Instrucciones.Coincidencia import Coincidencia
from Interpreter.Instrucciones.Condicionales.Match import Match
from Interpreter.Instrucciones.Transferencia.Break import Break
from Interpreter.Instrucciones.Transferencia.Return import Return
from Interpreter.Instrucciones.Condicionales.ClaseIf import ClaseIf
from Interpreter.Instrucciones.Transferencia.Continue import Continue
from Interpreter.Expresiones.Operaciones.Aritmeticas import Aritmeticas
from Interpreter.Expresiones.Operaciones.Relacionales import Relacionales

tokens = lexer.tokens

# PRECEDENCIA
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('nonassoc', 'IGUAL_IGUAL', 'NO_IGUAL', 'MENOR', 'MAYOR', 'MENOR_IGUAL', 'MAYOR_IGUAL'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'MULTI', 'DIV', 'MODULO'),
    ('right', 'NOT', 'UNARIO')
)

def p_inicio(p):
    """
    inicio : instrucciones
    """
    p[0] = Ast(p[1])

def p_lista_instrucciones(p):
    """
    instrucciones : instrucciones instruccion
    """
    p[1].append(p[2])
    p[0] = p[1]

def p_instrucciones_instruccion(p):
    """
    instrucciones : instruccion
    """ 
    p[0] = [p[1]]

def p_instruccion(p):
    """
    instruccion : prints PT_COMA
                | declaracion PT_COMA
                | sent_if
                | match
                | expresion
                | return PT_COMA
                | break PT_COMA
                | continue PT_COMA
    """
    p[0] = p[1]

#=== INICIO INSTRUCCION PRINTLN ===
def p_instruccion_println(p):
    """
    prints : PRINTLN NOT PARA CADENA COMA list_exp PARC
    """
    p[0] = PrintLn(Primitivo(p[4], Tipos.STR_POINTER, p.lineno(1), p.lexpos(1)), p[6], p.lineno(1), p.lexpos(1))

def p_instruccion_println_cads(p):
    """
    prints : PRINTLN NOT PARA CADENA PARC
    """
    p[0] = PrintLn(Primitivo(p[4], Tipos.STR_POINTER, p.lineno(1), p.lexpos(1)), [], p.lineno(1), p.lexpos(1))

def p_println_listexp(p):
    """
    list_exp : list_exp COMA expresion
    """
    p[1].append(p[3])
    p[0] = p[1]

def p_println_listexp_exit(p):
    """
    list_exp : expresion
    """
    p[0] = [p[1]]
    
#=== FIN INSTRUCCION PRINTLN ===

# === INICIO DIFERENTES DECLARACIONES ===
def p_instruccion_declaracion(p):
    """
    declaracion : LET MUT ID DOS_PT tipo IGUAL valores
    """
    p[0] = Declaracion(
        True,
        p[3],
        Simbolo(Simbolos.VARIABLE, True, p[5], p[3], p[7]),
        p[5],
        p.lineno(1),
        p.lexpos(1)
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
        p.lexpos(1)
    )

def p_declaracion_3(p):
    """
    declaracion : LET MUT ID IGUAL valores
    """
    p[0] = Declaracion(
        True,
        p[3],
        Simbolo(Simbolos.VARIABLE, True, p[3], None, p[5]),
        None,
        p.lineno(1),
        p.lexpos(1)
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
        p.lexpos(1)
    )

def p_declaracion_5(p):
    """
    declaracion : LET ID DOS_PT tipo IGUAL valores
    """
    p[0] = Declaracion(
        False,
        p[2],
        Simbolo(Simbolos.VARIABLE, False, p[2], p[4], p[6]),
        p[4],
        p.lineno(1),
        p.lexpos(1)
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
        p.lexpos(1)
    )

def p_declaracion_7(p):
    """
    declaracion : LET ID IGUAL valores
    """
    p[0] = Declaracion(
        False,
        p[2],
        Simbolo(Simbolos.VARIABLE, False, p[2], None, p[4]),
        None,
        p.lineno(1),
        p.lexpos(1)
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
        p.lexpos(1)
    )

def p__declaracion_asignacion(p):
    """
    declaracion : ID IGUAL valores
    """
    p[0] = Declaracion(
        False,
        p[1],
        Simbolo(Simbolos.VARIABLE, False, p[1], None, p[3]),
        None,
        p.lineno(1),
        p.lexpos(1)
    )

def p_declaracion_valores(p):
    """
    valores : expresion
            | sent_if
            | match
    """
    p[0] = p[1]
# === FIN DIFERENTES DECLARACIONES ===

# === INICIO INSTRUCCION IF-ELSE ===
def p_instruccion_sent_if(p):
    """
    sent_if : IF expresion statement sent_else
    """
    p[0] = ClaseIf(p[2], p[3], p[4], p.lineno(1), p.lexpos(1))

def p_sent_else(p):
    """
    sent_else : ELSE statement
            | ELSE sent_if
    """
    p[0] = p[2]

def p_sent_else_vacio(p):
    """
    sent_else : 
    """
    p[0] = None

# === FIN INSTRUCCION IF-ELSE

# === INICIO INSTRUCCION MATCH ===
def p_instruccion_match(p):
    """
    match : MATCH expresion casos_match
    """
    p[0] = Match(p[2], p[3], p.lineno(1), p.lexpos(1))

def p_match_casos(p):
    """
    casos_match : LLAVA lista_casos default LLAVC
    """
    p[2].append(p[3])
    p[0] = p[2]

def p_match_lista_casos(p):
    """
    lista_casos : lista_casos lista_expresiones ARROW statement COMA
                | lista_casos lista_expresiones ARROW instruccion COMA
    """
    p[1].append(Coincidencia(p[2], p[4], p.lineno(1), p.lexpos(1)))
    p[0] = p[1]

def p_match_lista_casos_salida(p):
    """
    lista_casos : lista_expresiones ARROW statement COMA
                | lista_expresiones ARROW instruccion COMA
    """
    p[0] = [Coincidencia(p[1], p[3], p.lineno(1), p.lexpos(1))]

def p_match_lista_expresiones(p):
    """
    lista_expresiones : lista_expresiones SEP_MATCH expresion
    """
    p[1].append(p[3])
    p[0] = p[1]

def p_match_lista_expresiones2(p):
    """
    lista_expresiones : expresion
    """
    p[0] = [p[1]]

def p_match_default(p):
    """
    default : GUION_B ARROW statement COMA
            | GUION_B ARROW instruccion COMA
    """
    p[0] = Coincidencia([], p[3], p.lineno(1), p.lexpos(1))

# === FIN INSTRUCCION MATCH ===

# === INICIO INSTRUCCION RETURN ===
def p_instruccion_return(p):
    """
    return : RETURN
            | RETURN expresion
    """
    if len(p) == 2:
        p[0] = Return(None, p.lineno(1), p.lexpos(1))
    else:
        p[0] = Return(p[2], p.lineno(1), p.lexpos(1))

# === FIN INSTRUCCION RETURN ===

# === INICIO INSTRUCCION BREAK ===
def p_instruccion_break(p):
    """
    break : BREAK
    """
    p[0] = Break(p.lineno(1), p.lexpos(1))

# === FIN INSTRUCCION BREAK ===

# === INICIO INSTRUCCION CONTINUE ===
def p_instruccion_continue(p):
    """
    continue : CONTINUE
    """
    p[0] = Continue(p.lineno(1), p.lexpos(1))

# === FIN INSTRUCCION CONTINUE ===

# === INICIO STATEMENT ===
def p_statement(p):
    """
    statement : LLAVA instrucciones LLAVC
    """
    p[0] = Statement(p[2], p.lineno(1), p.lexpos(1))

def p_statement_vacio(p):
    """
    statement : LLAVA LLAVC
    """
    p[0] = Statement([], p.lineno(1), p.lexpos(1))

# === FIN STATEMENT ===

def p_tipo(p):
    """
    tipo : I64
        | F64
        | BOOL
        | STRING
        | STR
        | CHAR
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
    elif p[1] == 'char':
        p[0] = Tipos.CARACTER

# === INICIO ARITMETICAS
def p_exp_aritmeticas(p):
    """
    expresion : MENOS expresion %prec UNARIO
            | expresion MAS expresion
            | expresion MENOS expresion
            | expresion MULTI expresion
            | expresion DIV expresion
            | expresion MODULO expresion
    """
    if len(p) == 3:
        p[0] = Aritmeticas(exp1=p[2], operador='UNARIO', exp2=None, expU=True, linea=p.lineno(1), columna = p.lexpos(1))
    else:
        p[0] = Aritmeticas(exp1 = p[1], operador = p[2], exp2 = p[3], expU = False, linea = p.lineno(1), columna = p.lexpos(1))

def p_exp_potencia(p):
    """
    expresion : I64 DOS_PT DOS_PT POW PARA expresion COMA expresion PARC
    """
    p[0] = Aritmeticas(exp1 = p[6], operador = '^', exp2 = p[8], expU = False, linea = p.lineno(1), columna = p.lexpos(1))

def p_exp_parentesis(p):
    """
    expresion : PARA expresion PARC
    """
    p[0] = p[2]

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
    p[0] = Relacionales(exp1 = p[1], operador = p[2], exp2 = p[3], linea = p.lineno(1), columna = p.lexpos(1))
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
    expresion : NOT expresion %prec NOT
    """
    p[0] = Logicas(exp1 = None, operador = p[1], exp2 = p[2], linea = p.lineno(1), columna = p.lexpos(1))

# === FIN LOGICAS ===

# === INICIO TIPOS DE DATO ===
def p_exp_primtivos(p):
    """
    expresion : ENTERO
            | DECIMAL
            | ID
            | CADENA 
            | CARACTER
            | TRUE
            | FALSE
    """
    if p.slice[1].type == 'ENTERO':
        p[0] = Primitivo(p[1], Tipos.INT64, p.lineno(1), p.lexpos(1))
    elif p.slice[1].type == 'DECIMAL':
        p[0] = Primitivo(p[1], Tipos.FLOAT64, p.lineno(1), p.lexpos(1))
    elif p.slice[1].type == 'ID':
        p[0] = Identificador(p[1], p.lineno(1), p.lexpos(1))
    elif p.slice[1].type == 'CADENA':
        p[0] = Primitivo(p[1], Tipos.STR_POINTER, p.lineno(1), p.lexpos(1))
    elif p.slice[1].type == 'CARACTER':
        p[0] = Primitivo(p[1], Tipos.CARACTER, p.lineno(1), p.lexpos(1))
    elif p.slice[1].type == 'TRUE':
        p[0] = Primitivo(True, Tipos.BOOLEAN, p.lineno(1), p.lexpos(1))
    elif p.slice[1].type == 'FALSE':
        p[0] = Primitivo(False, Tipos.BOOLEAN, p.lineno(1), p.lexpos(1))

def p_exp_cadena_toowned(p):
    """
    expresion : expresion PUNTO TO_OWNED PARA PARC
    """
    p[0] = ToOwned(p[1], Tipos.STR_BUFFER, p.lineno(1), p.lexpos(1))

def p_exp_cadena_tostring(p):
    """
    expresion : expresion PUNTO TO_STRING PARA PARC
    """
    p[0] = ToString(p[1], Tipos.STR_BUFFER, p.lineno(1), p.lexpos(1))

def p_exp_absoluto(p):
    """
    expresion : expresion PUNTO ABSOLUTO PARA PARC
    """
    p[0] = Absoluto(p[1], p.lineno(1), p.lexpos(1))

def p_exp_raiz(p):
    """
    expresion : expresion PUNTO RAIZ PARA PARC
    """
    p[0] = Raiz(p[1], Tipos.FLOAT64, p.lineno(1), p.lexpos(1))

def p_exp_casteo(p):
    """
    expresion : expresion AS F64
            | expresion AS I64
    """
    if p[3] == 'f64':
        p[0] = Casteo(p[1], Tipos.FLOAT64, p.lineno(1), p.lexpos(1))
    elif p[3] == 'i64':
        p[0] = Casteo(p[1], Tipos.INT64, p.lineno(1), p.lexpos(1))

# === FIN TIPOS DE DATO ===

# Error sintactico
def p_error(p):
    print(f'Error de sintaxis {p.value!r} en la linea {p.lineno} columna {p.lexpos}')

# Build the parser
parser = yacc(debug=True)