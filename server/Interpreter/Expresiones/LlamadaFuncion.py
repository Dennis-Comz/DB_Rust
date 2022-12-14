from Interpreter.Expresiones.Expresion import Expresion
from Interpreter.Instrucciones.Instruccion import Instruccion
from Interpreter.TablaSimbolos.TablaSimbolos import TablaSimbolos
from Interpreter.Driver.Driver import Driver
from Interpreter.TablaSimbolos.Tipos import Tipos
from Interpreter.TablaSimbolos.Simbolo import Simbolo, Simbolos
from Interpreter.Expresiones.Identificador import Identificador
from static import simbs

class LlamadaFuncion(Instruccion, Expresion):
    def __init__(self, id:str, parametros, linea:int, columna: int):
        self.id = id
        self.parametros = parametros
        self.linea = linea
        self.columna = columna
        self.salida = None

    def ejecutar(self, driver: Driver, ts: TablaSimbolos, errores):
        try:
            funcion = ts.buscarFuncion(self.id)
            
            if funcion != None:
                #Verificacion de que la cantidad de parametros declarados sean igual a los enviados
                if len(self.parametros) == len(funcion.parametros):
                    ts_local = TablaSimbolos(ts, "FUNCION_"+self.id.capitalize())
                    if funcion.nombre == "main":
                        ts_local = TablaSimbolos(ts, "MAIN")

                    #Ciclo que verifica que los tipos de los parametros coincidan con los aceptados en la declaracion
                    for i in range(0, len(self.parametros)):
                        tipoParam = self.parametros[i].getTipo(driver, ts, errores)
                        if tipoParam != funcion.parametros[i].type:
                            driver.append(f'Error Semantico, se esperaba parametro {funcion.parametros[i].type} se obtuvo {tipoParam}, linea {self.linea}, columna {self.columna}')
                            raise Exception({"tipo":"Semantico", "descripcion":f"Se obtuvo parametro tipo {tipoParam}, se esperaba {funcion.parametros[i].type}", "linea": str(self.linea), "columna":str(self.columna), "ambito": ts_local.env})
                    #Ciclo que agrega los parametros enviados a la tabla de simbolos local
                    for i in range(0, len(self.parametros)):
                        valorParam = self.parametros[i].getValor(driver, ts, errores)
                        ts_local.add(funcion.parametros[i].id, Simbolo(Simbolos.VARIABLE, True, funcion.parametros[i].id, funcion.parametros[i].type, valorParam))

                    if funcion.tipo == Tipos.VOID:
                        #Ciclo para verificar si la funcion contiene parametros por valor o por referencia
                        for i in range(0, len(self.parametros)):
                            if funcion.parametros[i].mutable:
                                if funcion.parametros[i].isArray:
                                    #Agregar a tabla de simbolos de arreglos
                                    pass
                                else:
                                #Si no es instancia de identificador, es decir se envia un valor normal, es un error semantico ya que se esperaba una
                                #variable a la que se le pueda cambiar su valor
                                    if isinstance(self.parametros[i], Identificador):
                                        valor = ts.buscar(self.parametros[i].identificador)
                                        val_local = ts_local.buscar(funcion.parametros[i].id)
                                        valor.valor = val_local.valor
                                        ts.add(self.parametros[i].identificador, valor)
                                    else:
                                        driver.append(f'Error Semantico, Se esperaba recibir un identificador y se obtuvo un valor, linea {self.linea}, columna {self.columna}')
                                        raise Exception({"tipo":"Semantico", "descripcion":f"Se esperaba recibir un identificador y se obtuvo un valor", "linea": str(self.linea), "columna":str(self.columna), "ambito": ts_local.env})
                        funcion.cuerpo.ejecutar(driver, ts_local, errores)
                    else:
                        result = funcion.cuerpo.ejecutar(driver, ts_local, errores)
                        if result != None and result["return"]:
                            for i in range(0, len(self.parametros)):
                                if funcion.parametros[i].mutable:
                                    if funcion.parametros[i].isArray:
                                        #Agregar a tabla de simbolos de arreglos
                                        pass
                                    else:
                                        if isinstance(self.parametros[i], Identificador):
                                            valor = ts.buscar(self.parametros[i].identificador)
                                            val_local = ts_local.buscar(funcion.parametros[i].id)
                                            valor.valor = val_local.valor
                                            ts.add(self.parametros[i].identificador, valor)
                                        else:
                                            driver.append(f'Error Semantico, Se esperaba recibir un identificador y se obtuvo un valor, linea {self.linea}, columna {self.columna}')
                                            raise Exception({"tipo":"Semantico", "descripcion":f"Se esperaba recibir un identificador y se obtuvo un valor", "linea": str(self.linea), "columna":str(self.columna), "ambito": ts_local.env})

                            tipoExp = result["expTipo"]
                            valExp = result["expValor"]
                            if tipoExp == funcion.tipo:
                                return {"tipo": tipoExp, "valor":valExp}
                            else:
                                driver.append(f'Error Semantico, se esperaba tipo de retorno {funcion.tipo} se obtuvo {tipoExp}, linea {self.linea}, columna {self.columna}')
                                raise Exception({"tipo":"Semantico", "descripcion":f"Se obtuvo retorno tipo {tipoExp}, se esperaba {funcion.tipo}", "linea": str(self.linea), "columna":str(self.columna), "ambito": ts_local.env})
                    simbs.append(ts_local)
                else:
                    driver.append(f'Error Semantico, La funcion {self.id} requiere {len(funcion.parametros)} parametros, se obtuvieron {len(self.parametros)} parametros, linea {self.linea}, columna {self.columna}')
                    raise Exception({"tipo":"Semantico", "descripcion":f"La funcion {self.id} requiere {len(funcion.parametros)} parametros, se obtuvieron {len(self.parametros)} parametros", "linea": str(self.linea), "columna":str(self.columna), "ambito": ts_local.env})
            else:
                    driver.append(f'Error Semantico, La funcion a llamar no existe, linea {self.linea}, columna {self.columna}')
                    raise Exception({"tipo":"Semantico", "descripcion":f"La funcion a llamar no existe", "linea": str(self.linea), "columna":str(self.columna), "ambito": ts_local.env})

        except Exception as d:
            if type(d.args[0]) == dict:
                errores.append(d.args[0])
            pass

    def getTipo(self, driver, ts, errores):
        funcion = ts.buscarFuncion(self.id)
#        ts_local = ts
        ts_local = TablaSimbolos(ts, "FUNCION_"+self.id.capitalize())

        if funcion != None:
            if len(self.parametros) == len(funcion.parametros):
                for i in range(0, len(self.parametros)):
                    tipoParam = self.parametros[i].getTipo(driver, ts, errores)
                    if tipoParam != funcion.parametros[i].type:
                        driver.append(f'Error Semantico, se esperaba parametro {funcion.parametros[i].type} se obtuvo {tipoParam}, linea {self.linea}, columna {self.columna}')
                        raise Exception({"tipo":"Semantico", "descripcion":f"Se obtuvo parametro tipo {tipoParam}, se esperaba {funcion.parametros[i].type}", "linea": str(self.linea), "columna":str(self.columna)})
                    else:
                        valorParam = self.parametros[i].getValor(driver, ts, errores)
                        ts_local.add(funcion.parametros[i].id, Simbolo(Simbolos.VARIABLE, True, funcion.parametros[i].id, funcion.parametros[i].type, valorParam))
                if funcion.tipo == Tipos.VOID:
                    for i in range(0, len(self.parametros)):
                        if funcion.parametros[i].mutable:
                            if funcion.parametros[i].isArray:
                                #Agregar a tabla de simbolos de arreglos
                                pass
                            else:
                                if isinstance(self.parametros[i], Identificador):
                                    valor = ts.buscar(self.parametros[i].identificador)
                                    val_local = ts_local.buscar(funcion.parametros[i].id)
                                    valor.valor = val_local.valor
                                    ts.add(self.parametros[i].identificador, valor)
                                else:
                                    driver.append(f'Error Semantico, Se esperaba recibir un identificador y se obtuvo un valor, linea {self.linea}, columna {self.columna}')
                                    raise Exception({"tipo":"Semantico", "descripcion":f"Se esperaba recibir un identificador y se obtuvo un valor", "linea": str(self.linea), "columna":str(self.columna), "ambito": ts_local.env})

                    return funcion.cuerpo.ejecutar(driver, ts_local, errores)
                else:
                    result = funcion.cuerpo.ejecutar(driver, ts_local, errores)
                    if result != None:
                        for i in range(0, len(self.parametros)):
                            if funcion.parametros[i].mutable:
                                if funcion.parametros[i].isArray:
                                    #Agregar a tabla de simbolos de arreglos
                                    pass
                                else:
                                    if isinstance(self.parametros[i], Identificador):
                                        valor = ts.buscar(self.parametros[i].identificador)
                                        val_local = ts_local.buscar(funcion.parametros[i].id)
                                        valor.valor = val_local.valor
                                        ts.add(self.parametros[i].identificador, valor)
                                    else:
                                        driver.append(f'Error Semantico, Se esperaba recibir un identificador y se obtuvo un valor, linea {self.linea}, columna {self.columna}')
                                        raise Exception({"tipo":"Semantico", "descripcion":f"Se esperaba recibir un identificador y se obtuvo un valor", "linea": str(self.linea), "columna":str(self.columna), "ambito": ts_local.env})

                        self.salida = result
                        return result["expTipo"]
            else:
                driver.append(f'Error Semantico, La cantidad de parametros no es correcta, linea {self.linea}, columna {self.columna}')
                raise Exception({"tipo":"Semantico", "descripcion":f"La cantidad de parametros proporcionada no es correcta", "linea": str(self.linea), "columna":str(self.columna)})
        else:
                driver.append(f'Error Semantico, La funcion a llamar no existe, linea {self.linea}, columna {self.columna}')
                raise Exception({"tipo":"Semantico", "descripcion":f"La funcion a llamar no existe", "linea": str(self.linea), "columna":str(self.columna)})

    def getValor(self, driver, ts, errores):
        return self.salida["expValor"]