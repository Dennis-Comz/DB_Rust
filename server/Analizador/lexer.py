# Declaracion de tokens
from plyFiles.ply import lex

reservadas = {
    'Print': 'PRINT',
    'i64': 'I64',
    'pow': 'POW'
}

tokens = [
            'DECIMAL',
            'ENTERO',
            'MAS',
            'MENOS',
            'MULTI',
            'DIV',
            'MODULO',
            'PT_COMA',
            'PARA',
            'PARC',
            'COMA',
            'DOS_PT'
] + list(reservadas.values())

# Caracteres ignorados
t_ignore = '[\t ]'

# Tokens con Regex
t_MAS = r'\+'
t_MENOS = r'-'
t_MULTI = r'\*'
t_DIV = r'/'
t_MODULO = r'\%'
t_PARA = r'\('
t_PARC = r'\)'
t_PT_COMA = r'\;'
t_COMA = r'\,'
t_DOS_PT = r'\:'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value, 'ID')  # Check for reserved words
    return t

#==== TIPOS DE DATO =====
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
    t.value = int(t.value)
    return t
#==== FIN TIPOS DE DATO =====

# === Fin token potencia ===
# Ignora y hace una accion
def t_ignorar_salto(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

def find_column(input, token):
     line_start = input.rfind('\n', 0, token.lexpos) + 1
     return (token.lexpos - line_start) + 1

# Manejo de errores lexicos
def t_error(t):
    print(f'Error lexico {t.value[0]!r} en la linea {t.lexer.lineno} columna {find_column(t.value, t)}')
    t.lexer.skip(1)


lex.lex()