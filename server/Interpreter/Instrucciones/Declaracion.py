from fileinput import filename
from Interpreter.TablaSimbolos.TablaSimbolos import TablaSimbolos
from Interpreter.TablaSimbolos.Simbolo import Simbolo, Simbolos
from Interpreter.Instrucciones.Instruccion import Instruccion
from Interpreter.TablaSimbolos.Tipos import Tipo
from Interpreter.Driver.Driver import Driver

class Declaracion(Instruccion):

    def __init__(self, muteable: bool, identificador: str, variable: Simbolo, tipo: Tipo, linea: int, columna: int):
        self.muteable = muteable
        self.identificador = identificador
        self.variable = variable
        self.tipo = tipo
        self.linea = linea
        self.columna = columna

    def ejecutar(self, driver: Driver, ts: TablaSimbolos):
        tipo_var = self.variable.valor.getTipo(driver, ts)
        valor_var = self.variable.valor.getValor(driver, ts)

        # Verificar el tipo
        if self.tipo != tipo_var:
            driver.append(f"La variable no coincide con el tipo del valor linea: {self.linea}, columna: {self.columna}")
            return

        # Agregar a tabla de simbolos
        simbolo = ts.buscar(self.identificador)

        if simbolo is None:
            # Si no existe la variable
            simbolo_nuevo = Simbolo(Simbolos.VARIABLE, self.tipo, self.identificador, valor_var)
            ts.add(self.identificador, simbolo_nuevo)
        else:
            # Si ya existe la variable
            simbolo.valor = valor_var
            ts.add(self.identificador, simbolo)