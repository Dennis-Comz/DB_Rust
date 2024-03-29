from Interpreter.TablaSimbolos.TablaSimbolos import TablaSimbolos
from Interpreter.TablaSimbolos.Simbolo import Simbolo, Simbolos
from Interpreter.Instrucciones.Instruccion import Instruccion
from Interpreter.TablaSimbolos.Tipos import Tipo
from Interpreter.Driver.Driver import Driver
from Interpreter.TablaSimbolos.Arreglo import Arreglo

class Declaracion(Instruccion):

    def __init__(self, muteable: bool, identificador: str, variable: Simbolo, tipo, linea: int, columna: int):
        self.muteable = muteable
        self.identificador = identificador
        self.variable = variable
        self.tipo = tipo
        self.linea = linea
        self.columna = columna

    def ejecutar(self, driver: Driver, ts: TablaSimbolos, errores):
        try:
            #Validacion de si la variable enviada existe
            simbolo = ts.buscar(self.identificador)

            #Si el simbolo no se encuentra es posible que se haga referencia a un arreglo
            #ID = ID
            if simbolo is None:
                simbolo = ts.buscarArreglo(self.identificador)
                if simbolo is not None:
                    tipo_var = self.variable.valor.getTipo(driver, ts, errores)
                    valor_var = self.variable.valor.getValor(driver, ts, errores)
                    if simbolo.tipo == tipo_var:
                        simbolo.valores = valor_var
                        ts.addArreglo(self.identificador, simbolo)
                    else:
                        #error
                        pass

            #Validacion si la declaracion trae un valor
            if self.variable.valor != None:
                #Obteniendo tipo y valor de la variable
                tipo_var = self.variable.valor.getTipo(driver, ts, errores)
                valor_var = self.variable.valor.getValor(driver, ts, errores)
                    
                if simbolo is None:
                    #si aun no existe la variable se crea una
                    if self.tipo == None:
                        self.tipo = tipo_var
                    simbolo_nuevo = Simbolo(Simbolos.VARIABLE, self.muteable, self.identificador, self.tipo, valor_var)
                    ts.add(self.identificador, simbolo_nuevo)
                else:
                    if simbolo.tipo != None and simbolo.tipo != tipo_var:
                        driver.append(f'Error Semantico, el tipo de la expresion {tipo_var} no coincide con el tipo de la declaracion {simbolo.tipo}, linea {self.linea}, columna {self.columna}')
                        raise Exception({"tipo":"Semantico", "descripcion":f"el tipo de la expresion {tipo_var} no coincide con el tipo de la declaracion {simbolo.tipo}", "linea": str(self.linea), "columna":str(self.columna), "ambito": ts.env})
                    #si ya existe la variable se valida si esta puede cambiar su valor
                            
                    if simbolo.valor == None and simbolo.mutable is False:
                            simbolo.valor = valor_var
                            #LET ID; ID = [];
                            #Se inicializa variable vacia y se le asigna un arreglo
                            if type(valor_var) == list:
                                dimension = 1
                                if type(valor_var[0]) == list:
                                    dimension = len(valor_var)
                                    
                                ts.addArreglo(self.identificador, Arreglo(Simbolos.ARREGLO, False, self.identificador, tipo_var, dimension, valor_var))
                                ts.eliminar_variable(self.identificador)
                            else:
                                ts.add(self.identificador, simbolo)
                    else:
                        if simbolo.mutable:
                            simbolo.valor = valor_var
                            simbolo.tipo = tipo_var
                            #LET ID; ID = [];
                            #Se inicializa variable vacia y se le asigna un arreglo
                            if type(valor_var) == list:
                                dimension = 1
                                if type(valor_var[0]) == list:
                                    dimension = len(valor_var)

                                ts.addArreglo(self.identificador, Arreglo(Simbolos.ARREGLO, False, self.identificador, tipo_var, dimension, valor_var))
                                ts.eliminar_variable(self.identificador)
                            else:
                                ts.add(self.identificador, simbolo)
                        else:
                            driver.append(f'Error semantico, no se le puede cambiar su valor a una variable no mutable, linea {self.linea}, columna {self.columna}')
                            raise Exception({"tipo":"Semantico", "descripcion":f"no se le puede cambiar su valor a una variable no mutable", "linea": str(self.linea), "columna":str(self.columna), "ambito": ts.env})
            else:
                if simbolo is None:
                    #si aun no existe la variable se crea una
                    simbolo_nuevo = Simbolo(Simbolos.VARIABLE, self.muteable, self.identificador, self.tipo, None)
                    ts.add(self.identificador, simbolo_nuevo)
                else:
                    driver.append(f'Error semantico, la variable ya ha sido declarada, linea {self.linea}, columna {self.columna}')
                    raise Exception({"tipo":"Semantico", "descripcion":f"la variable ya ha sido declarada", "linea": str(self.linea), "columna":str(self.columna), "ambito": ts.env})
        except Exception as d:
            if type(d.args[0]) == dict:
                errores.append(d.args[0])
            pass
