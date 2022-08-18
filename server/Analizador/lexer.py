# Declaracion de tokens
from dataclasses import replace
from plyFiles.ply import lex

reservadas = {
    'print': 'PRINT',
    'i64': 'I64',
    'f64': 'F64',
    'String': 'STRING',
    'char': 'CHAR',
    'bool': 'BOOL',
    'pow': 'POW',
    'true': 'TRUE',
    'false': 'FALSE',
    'to_owned': 'TO_OWNED',
    'to_string': 'TO_STRING',
    'let': 'LET',
    'mut': 'MUT'
}

tokens = [
            'DECIMAL',
            'ENTERO',
            'CARACTER',
            'CADENA',
            'STR',
            'MAS',
            'MENOS',
            'MULTI',
            'DIV',
            'MODULO',
            'PT_COMA',
            'PUNTO',
            'PARA',
            'PARC',
            'COMA',
            'DOS_PT',
            'IGUAL_IGUAL',
            'NO_IGUAL',
            'MAYOR',
            'MENOR',
            'MAYOR_IGUAL',
            'MENOR_IGUAL',
            'AND',
            'OR',
            'NOT',
            'IGUAL',
            'ID'
] + list(reservadas.values())

# Caracteres ignorados
t_ignore = '[\r\t ]'

# Tokens con Regex
t_MAS = r'\+'
t_MENOS = r'-'
t_MULTI = r'\*'
t_DIV = r'/'
t_MODULO = r'\%'
t_PARA = r'\('
t_PARC = r'\)'
t_PT_COMA = r'\;'
t_PUNTO = r'\.'
t_COMA = r'\,'
t_DOS_PT = r'\:'
t_IGUAL_IGUAL = r'\=\='
t_NO_IGUAL = r'\!\='
t_MAYOR = r'\>'
t_MENOR = r'\<'
t_MAYOR_IGUAL = r'\>\='
t_MENOR_IGUAL = r'\<\='
t_STR = r'\&str'
t_AND = r'\&\&'
t_OR = r'\|\|'
t_NOT = r'\!'
t_IGUAL = r'\='

def t_DECIMAL(t):
    r"""\d+\.\d+"""
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r"""\d+"""
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_ID(t):
    r"""[a-zA-Z_][a-zA-Z_0-9]*"""
    t.type = reservadas.get(t.value, 'ID')
    return t

def t_CADENA(t):
    r"""\"[^\"\n]*\""""
    t.value = t.value[1:-1]
    return t

def t_CARACTER(t):
    r"""\'[^\']\'"""
    t.value = t.value[1:-1]
    return t

def t_COMENTARIO(t):
    r"""\/\/.*"""


# Ignora y hace una accion
def t_ignorar_salto(t):
    r"""\n+"""
    t.lexer.lineno += t.value.count("\n")

def find_column(input, token):
     line_start = input.rfind('\n', 0, token.lexpos) + 1
     return (token.lexpos - line_start) + 1

# Manejo de errores lexicos
def t_error(t):
    print(f'Error lexico {t.value[0]!r} en la linea {t.lexer.lineno} columna {find_column(t.value, t)}')
    t.lexer.skip(1)


lex.lex()