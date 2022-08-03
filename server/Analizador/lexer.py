# Declaracion de tokens
from plyFiles.ply import lex

reservadas = {
    'Print': 'PRINT'
}

tokens = [
#TIPOS DE DATO
            'DECIMAL',
            'ENTERO',
#OPERACIONES ARITMETICAS
            'MAS',
            'MENOS',
            'MULTI',
            'DIV',
            'POTENCIA',
            'MODULO',
#TOKENS ESPECIALES
            'PT_COMA',
            'PARA',
            'PARC'
] + list(reservadas.values())

# Caracteres ignorados
t_ignore = '[\t ]'

# Tokens con Regex
t_MAS = r'\+'
t_MENOS = r'-'
t_MULTI = r'\*'
t_DIV = r'/'
t_POTENCIA = r'\^'
t_MODULO = r'\%'
t_PARA = r'\('
t_PARC = r'\)'
t_PT_COMA = r'\;'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value, 'ID')  # Check for reserved words
    return t

#==== TIPOS DE DATO =====
def t_ENTERO(t):
    r"""\d+"""
    t.value = int(t.value)
    return t

def t_DECIMAL(t):
    r"""\d+\.\d+"""
    try:
        t.value = float(t.value)
    except ValueError:
        print("El valor del float es muy largo %d", t.value)
        t.value = 0
    return 0
#==== FIN TIPOS DE DATO =====

# Ignora y hace una accion
def t_ignorar_salto(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

# Manejo de errores lexicos
def t_error(t):
    print(f'Caracter no reconocido {t.value[0]!r} en la linea {t.lexer.lineno}')
    t.lexer.skip(1)


lex.lex()