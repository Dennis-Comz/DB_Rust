from Interpreter.Expresiones.Operaciones.OperacionRelacional import OperacionRelacional, Operador, getOperacion
from Interpreter.TablaSimbolos.Tipos import Tipos, definirTipo

class Relacionales(OperacionRelacional):

    def getTipo(self, driver, ts, errores):
        value = self.getValor(driver, ts, errores)
        return definirTipo(value)

    def getValor(self, driver, ts, errores):
        tipo_exp1 = self.exp1.getTipo(driver, ts, errores)
        tipo_exp2 = self.exp2.getTipo(driver, ts, errores)

        if self.operador == Operador.IGUAL_IGUAL:
            if tipo_exp1 == Tipos.INT64 and tipo_exp2 == Tipos.INT64:
                return self.exp1.getValor(driver, ts, errores) == self.exp2.getValor(driver,ts, errores)
            elif tipo_exp1 == Tipos.FLOAT64 and tipo_exp2 == Tipos.FLOAT64:
                return self.exp1.getValor(driver, ts, errores) == self.exp2.getValor(driver,ts, errores)
            elif tipo_exp1 == Tipos.BOOLEAN and tipo_exp2 == Tipos.BOOLEAN:
                return self.exp1.getValor(driver, ts, errores) == self.exp2.getValor(driver,ts, errores)
            elif tipo_exp1 == Tipos.STR_BUFFER and tipo_exp2 == Tipos.STR_BUFFER:
                return self.exp1.getValor(driver, ts, errores) == self.exp2.getValor(driver,ts, errores)
            elif tipo_exp1 == Tipos.STR_POINTER and tipo_exp2 == Tipos.STR_POINTER:
                return self.exp1.getValor(driver, ts, errores) == self.exp2.getValor(driver,ts, errores)
            elif tipo_exp1 == Tipos.STR_BUFFER and tipo_exp2 == Tipos.STR_POINTER:
                return self.exp1.getValor(driver, ts, errores) == self.exp2.getValor(driver,ts, errores)
            elif tipo_exp1 == Tipos.STR_POINTER and tipo_exp2 == Tipos.STR_BUFFER:
                return self.exp1.getValor(driver, ts, errores) == self.exp2.getValor(driver,ts, errores)
            else:
                driver.append(f'Error Semantico, No se pueden comparar {tipo_exp1} con {tipo_exp2}, linea {self.exp2.linea}, columna {self.exp2.columna}')
                raise Exception({"tipo":"Semantico", "descripcion":f"No se pueden comparar {tipo_exp1} con {tipo_exp2}", "linea": str(self.exp2.linea), "columna":str(self.exp2.columna), "ambito": ts.env})
        elif self.operador == Operador.NO_IGUAL:
            if tipo_exp1 == Tipos.INT64 and tipo_exp2 == Tipos.INT64:
                return self.exp1.getValor(driver, ts, errores) != self.exp2.getValor(driver,ts, errores)
            elif tipo_exp1 == Tipos.FLOAT64 and tipo_exp2 == Tipos.FLOAT64:
                return self.exp1.getValor(driver, ts, errores) != self.exp2.getValor(driver,ts, errores)
            elif tipo_exp1 == Tipos.BOOLEAN and tipo_exp2 == Tipos.BOOLEAN:
                return self.exp1.getValor(driver, ts, errores) != self.exp2.getValor(driver,ts, errores)
            elif tipo_exp1 == Tipos.STR_BUFFER and tipo_exp2 == Tipos.STR_BUFFER:
                return self.exp1.getValor(driver, ts, errores) != self.exp2.getValor(driver,ts, errores)
            elif tipo_exp1 == Tipos.STR_POINTER and tipo_exp2 == Tipos.STR_POINTER:
                return self.exp1.getValor(driver, ts, errores) != self.exp2.getValor(driver,ts, errores)
            elif tipo_exp1 == Tipos.STR_BUFFER and tipo_exp2 == Tipos.STR_POINTER:
                return self.exp1.getValor(driver, ts, errores) != self.exp2.getValor(driver,ts, errores)
            elif tipo_exp1 == Tipos.STR_POINTER and tipo_exp2 == Tipos.STR_BUFFER:
                return self.exp1.getValor(driver, ts, errores) != self.exp2.getValor(driver,ts, errores)
            else:
                driver.append(f'Error Semantico, No se pueden comparar {tipo_exp1} con {tipo_exp2}, linea {self.exp2.linea}, columna {self.exp2.columna}')
                raise Exception({"tipo":"Semantico", "descripcion":f"No se pueden comparar {tipo_exp1} con {tipo_exp2}", "linea": str(self.exp2.linea), "columna":str(self.exp2.columna), "ambito": ts.env})

        elif self.operador == Operador.MAYOR:
            if tipo_exp1 == Tipos.INT64 and tipo_exp2 == Tipos.INT64:
                return self.exp1.getValor(driver, ts, errores) > self.exp2.getValor(driver,ts, errores)
            elif tipo_exp1 == Tipos.FLOAT64 and tipo_exp2 == Tipos.FLOAT64:
                return self.exp1.getValor(driver, ts, errores) > self.exp2.getValor(driver,ts, errores)
            elif tipo_exp1 == Tipos.BOOLEAN and tipo_exp2 == Tipos.BOOLEAN:
                return self.exp1.getValor(driver, ts, errores) > self.exp2.getValor(driver,ts, errores)
            elif tipo_exp1 == Tipos.STR_BUFFER and tipo_exp2 == Tipos.STR_BUFFER:
                return self.exp1.getValor(driver, ts, errores) > self.exp2.getValor(driver,ts, errores)
            elif tipo_exp1 == Tipos.STR_POINTER and tipo_exp2 == Tipos.STR_POINTER:
                return self.exp1.getValor(driver, ts, errores) > self.exp2.getValor(driver,ts, errores)
            elif tipo_exp1 == Tipos.STR_BUFFER and tipo_exp2 == Tipos.STR_POINTER:
                return self.exp1.getValor(driver, ts, errores) > self.exp2.getValor(driver,ts, errores)
            elif tipo_exp1 == Tipos.STR_POINTER and tipo_exp2 == Tipos.STR_BUFFER:
                return self.exp1.getValor(driver, ts, errores) > self.exp2.getValor(driver,ts, errores)
            else:
                driver.append(f'Error Semantico, No se pueden comparar {tipo_exp1} con {tipo_exp2}, linea {self.exp2.linea}, columna {self.exp2.columna}')
                raise Exception({"tipo":"Semantico", "descripcion":f"No se pueden comparar {tipo_exp1} con {tipo_exp2}", "linea": str(self.exp2.linea), "columna":str(self.exp2.columna), "ambito": ts.env})

        elif self.operador == Operador.MENOR:
            if tipo_exp1 == Tipos.INT64 and tipo_exp2 == Tipos.INT64:
                return self.exp1.getValor(driver, ts, errores) < self.exp2.getValor(driver,ts, errores)
            elif tipo_exp1 == Tipos.FLOAT64 and tipo_exp2 == Tipos.FLOAT64:
                return self.exp1.getValor(driver, ts, errores) < self.exp2.getValor(driver,ts, errores)
            elif tipo_exp1 == Tipos.BOOLEAN and tipo_exp2 == Tipos.BOOLEAN:
                return self.exp1.getValor(driver, ts, errores) < self.exp2.getValor(driver,ts, errores)
            elif tipo_exp1 == Tipos.STR_BUFFER and tipo_exp2 == Tipos.STR_BUFFER:
                return self.exp1.getValor(driver, ts, errores) < self.exp2.getValor(driver,ts, errores)
            elif tipo_exp1 == Tipos.STR_POINTER and tipo_exp2 == Tipos.STR_POINTER:
                return self.exp1.getValor(driver, ts, errores) < self.exp2.getValor(driver,ts, errores)
            elif tipo_exp1 == Tipos.STR_BUFFER and tipo_exp2 == Tipos.STR_POINTER:
                return self.exp1.getValor(driver, ts, errores) < self.exp2.getValor(driver,ts, errores)
            elif tipo_exp1 == Tipos.STR_POINTER and tipo_exp2 == Tipos.STR_BUFFER:
                return self.exp1.getValor(driver, ts, errores) < self.exp2.getValor(driver,ts, errores)
            else:
                driver.append(f'Error Semantico, No se pueden comparar {tipo_exp1} con {tipo_exp2}, linea {self.exp2.linea}, columna {self.exp2.columna}')
                raise Exception({"tipo":"Semantico", "descripcion":f"No se pueden comparar {tipo_exp1} con {tipo_exp2}", "linea": str(self.exp2.linea), "columna":str(self.exp2.columna), "ambito": ts.env})

        elif self.operador == Operador.MAYOR_IGUAL:
            if tipo_exp1 == Tipos.INT64 and tipo_exp2 == Tipos.INT64:
                return self.exp1.getValor(driver, ts, errores) >= self.exp2.getValor(driver,ts, errores)
            elif tipo_exp1 == Tipos.FLOAT64 and tipo_exp2 == Tipos.FLOAT64:
                return self.exp1.getValor(driver, ts, errores) >= self.exp2.getValor(driver,ts, errores)
            elif tipo_exp1 == Tipos.BOOLEAN and tipo_exp2 == Tipos.BOOLEAN:
                return self.exp1.getValor(driver, ts, errores) >= self.exp2.getValor(driver,ts, errores)
            elif tipo_exp1 == Tipos.STR_BUFFER and tipo_exp2 == Tipos.STR_BUFFER:
                return self.exp1.getValor(driver, ts, errores) >= self.exp2.getValor(driver,ts, errores)
            elif tipo_exp1 == Tipos.STR_POINTER and tipo_exp2 == Tipos.STR_POINTER:
                return self.exp1.getValor(driver, ts, errores) >= self.exp2.getValor(driver,ts, errores)
            elif tipo_exp1 == Tipos.STR_BUFFER and tipo_exp2 == Tipos.STR_POINTER:
                return self.exp1.getValor(driver, ts, errores) >= self.exp2.getValor(driver,ts, errores)
            elif tipo_exp1 == Tipos.STR_POINTER and tipo_exp2 == Tipos.STR_BUFFER:
                return self.exp1.getValor(driver, ts, errores) >= self.exp2.getValor(driver,ts, errores)
            else:
                driver.append(f'Error Semantico, No se pueden comparar {tipo_exp1} con {tipo_exp2}, linea {self.exp2.linea}, columna {self.exp2.columna}')
                raise Exception({"tipo":"Semantico", "descripcion":f"No se pueden comparar {tipo_exp1} con {tipo_exp2}", "linea": str(self.exp2.linea), "columna":str(self.exp2.columna), "ambito": ts.env})

        elif self.operador == Operador.MENOR_IGUAL:
            if tipo_exp1 == Tipos.INT64 and tipo_exp2 == Tipos.INT64:
                return self.exp1.getValor(driver, ts, errores) <= self.exp2.getValor(driver,ts, errores)
            elif tipo_exp1 == Tipos.FLOAT64 and tipo_exp2 == Tipos.FLOAT64:
                return self.exp1.getValor(driver, ts, errores) <= self.exp2.getValor(driver,ts, errores)
            elif tipo_exp1 == Tipos.BOOLEAN and tipo_exp2 == Tipos.BOOLEAN:
                return self.exp1.getValor(driver, ts, errores) <= self.exp2.getValor(driver,ts, errores)
            elif tipo_exp1 == Tipos.STR_BUFFER and tipo_exp2 == Tipos.STR_BUFFER:
                return self.exp1.getValor(driver, ts, errores) <= self.exp2.getValor(driver,ts, errores)
            elif tipo_exp1 == Tipos.STR_POINTER and tipo_exp2 == Tipos.STR_POINTER:
                return self.exp1.getValor(driver, ts, errores) <= self.exp2.getValor(driver,ts, errores)
            elif tipo_exp1 == Tipos.STR_BUFFER and tipo_exp2 == Tipos.STR_POINTER:
                return self.exp1.getValor(driver, ts, errores) <= self.exp2.getValor(driver,ts, errores)
            elif tipo_exp1 == Tipos.STR_POINTER and tipo_exp2 == Tipos.STR_BUFFER:
                return self.exp1.getValor(driver, ts, errores) <= self.exp2.getValor(driver,ts, errores)
            else:
                driver.append(f'Error Semantico, No se pueden comparar {tipo_exp1} con {tipo_exp2}, linea {self.exp2.linea}, columna {self.exp2.columna}')
                raise Exception({"tipo":"Semantico", "descripcion":f"No se pueden comparar {tipo_exp1} con {tipo_exp2}", "linea": str(self.exp2.linea), "columna":str(self.exp2.columna), "ambito": ts.env})

        else:
            driver.append(f'Error Semantico, La operacion {self.operador} no es soportado, linea {self.exp2.linea}, columna {self.exp2.columna}')
            raise Exception({"tipo":"Semantico", "descripcion":f"La operacion {self.operador} no es soportado", "linea": str(self.exp2.linea), "columna":str(self.exp2.columna), "ambito": ts.env})