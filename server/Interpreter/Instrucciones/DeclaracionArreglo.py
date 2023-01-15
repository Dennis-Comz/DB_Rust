from Interpreter.TablaSimbolos.TablaSimbolos import TablaSimbolos
from Interpreter.TablaSimbolos.Arreglo import Arreglo
from Interpreter.Instrucciones.Instruccion import Instruccion
from Interpreter.Driver.Driver import Driver
from Interpreter.TablaSimbolos.Tipos import Tipos
from Interpreter.TablaSimbolos.Simbolo import Simbolos

class DeclaracionArreglo(Instruccion):
    def __init__(self, mutable:bool, id:str, variable:Arreglo, tipo:Tipos, linea:int, columna:int) -> None:
        self.mutable = mutable
        self.id = id
        self.variable = variable
        self.tipo = tipo
        self.linea = linea
        self.columna = columna

    def ejecutar(self, driver: Driver, ts: TablaSimbolos, errores):
        try:
            #Validacion de si el arreglo ya existe
            simbolo = ts.buscarArreglo(self.id)

            #Validacion de si no se creo un arreglo vacio
            if self.variable.valores is not None:
                #Obteniendo tipo y valor de la variable
                tipo_var = self.variable.valores.getTipo(driver, ts, errores)
                valor_var = self.variable.valores.getValor(driver, ts, errores)

                if simbolo is None:
                    #si aun no existe la variable se crea una
                    if self.tipo == None:
                        self.tipo = tipo_var
                        simbolo_nuevo = Arreglo(Simbolos.ARREGLO, self.muteable, self.identificador, self.tipo, valor_var)
                        ts.addArreglo(self.identificador, simbolo_nuevo)
                else:
                    if simbolo.tipo != None and simbolo.tipo != tipo_var:
                        driver.append(f'Error Semantico, el tipo de la expresion {tipo_var} no coincide con el tipo de la declaracion {simbolo.tipo}, linea {self.linea}, columna {self.columna}')
                        raise Exception({"tipo":"Semantico", "descripcion":f"el tipo de la expresion {tipo_var} no coincide con el tipo de la declaracion {simbolo.tipo}", "linea": str(self.linea), "columna":str(self.columna), "ambito": ts.env})
                    #si ya existe la variable se valida si esta puede cambiar su valor
                            
                    if simbolo.valor == None and simbolo.mutable is False:
                            simbolo.valor = valor_var
                            ts.addArreglo(self.identificador, simbolo)
                    else:
                        if simbolo.mutable:
                            simbolo.valor = valor_var
                            simbolo.tipo = tipo_var
                            ts.addArreglo(self.identificador, simbolo)
                        else:
                            driver.append(f'Error semantico, no se le puede cambiar su valor a una variable no mutable, linea {self.linea}, columna {self.columna}')
                            raise Exception({"tipo":"Semantico", "descripcion":f"no se le puede cambiar su valor a una variable no mutable", "linea": str(self.linea), "columna":str(self.columna), "ambito": ts.env})
            else:
                if simbolo is None:
                    #si aun no existe la variable se crea una
                    simbolo_nuevo = Arreglo(Simbolos.ARREGLO, self.muteable, self.identificador, self.tipo, None)
                    ts.addArreglo(self.identificador, simbolo_nuevo)
                else:
                    driver.append(f'Error semantico, la variable ya ha sido declarada, linea {self.linea}, columna {self.columna}')
                    raise Exception({"tipo":"Semantico", "descripcion":f"la variable ya ha sido declarada", "linea": str(self.linea), "columna":str(self.columna), "ambito": ts.env})

        except Exception as d:
            if type(d.args[0]) == dict:
                errores.append(d.args[0])
            pass