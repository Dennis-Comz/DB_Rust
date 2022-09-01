from Interpreter.Expresiones.Operaciones.Operacion import Operacion, Operador, getOperacion
from Interpreter.TablaSimbolos.Tipos import Tipos, definirTipo

class Aritmeticas(Operacion):

    def getTipo(self, driver, ts):
        value = self.getValor(driver, ts)
        return definirTipo(value)

    # get valor con condicionales
    def getValor(self, driver, ts):
        tipo_exp1 = self.exp1.getTipo(driver, ts)
        tipo_exp2 = self.exp2.getTipo(driver, ts) if not self.expU else None

        if self.expU is not False:
            if self.operador == Operador.UNARIO:
                return - self.exp1.getValor(driver, ts)
            else:
                driver.append(f'Error Semantico, la operacion unaria solo acepta el operador -, linea {self.exp1.linea} columna {self.exp1.columna}')
                raise Exception(f'Error Semantico, la operacion unaria solo acepta el operador -, linea {self.exp1.linea} columna {self.exp1.columna}')
                
        if self.operador == Operador.SUMA:
            if tipo_exp1 == Tipos.INT64 and tipo_exp2 == Tipos.INT64:
                    return self.exp1.getValor(driver, ts) + self.exp2.getValor(driver, ts)
            elif tipo_exp1 == Tipos.FLOAT64 and tipo_exp2 == Tipos.FLOAT64:
                    return self.exp1.getValor(driver, ts) + self.exp2.getValor(driver, ts)
            elif tipo_exp1 == Tipos.STR_BUFFER and tipo_exp2 == Tipos.STR_POINTER:
                    return self.exp1.getValor(driver, ts) + self.exp2.getValor(driver, ts)
            else:
                driver.append(f'Error Semantico, No se pueden sumar {tipo_exp1} con {tipo_exp2}, linea {self.exp2.linea}, columna {self.exp2.columna}')
                raise Exception(f'Error Semantico, No se pueden sumar {tipo_exp1} con {tipo_exp2}, linea {self.exp2.linea}, columna {self.exp2.columna}')

        elif self.operador == Operador.RESTA:
            if tipo_exp1 == Tipos.INT64 and tipo_exp2 == Tipos.INT64:
                    return self.exp1.getValor(driver, ts) - self.exp2.getValor(driver, ts)
            elif tipo_exp1 == Tipos.FLOAT64 and tipo_exp2 == Tipos.FLOAT64:
                    return self.exp1.getValor(driver, ts) - self.exp2.getValor(driver, ts)
            else:
                driver.append(f'Error Semantico, No se pueden restar {tipo_exp1} con {tipo_exp2}, linea {self.exp2.linea}, columna {self.exp2.columna}')
                raise Exception(f'Error Semantico, No se pueden restar {tipo_exp1} con {tipo_exp2}, linea {self.exp2.linea}, columna {self.exp2.columna}')

        elif self.operador == Operador.MULTI:
            if tipo_exp1 == Tipos.INT64 and tipo_exp2 == Tipos.INT64:
                    return self.exp1.getValor(driver, ts) * self.exp2.getValor(driver, ts)
            elif tipo_exp1 == Tipos.FLOAT64 and tipo_exp2 == Tipos.FLOAT64:
                    return self.exp1.getValor(driver, ts) * self.exp2.getValor(driver, ts)
            else:
                driver.append(f'Error Semantico, No se pueden multiplicar {tipo_exp1} con {tipo_exp2}, linea {self.exp2.linea}, columna {self.exp2.columna}')
                raise Exception(f'Error Semantico, No se pueden multiplicar {tipo_exp1} con {tipo_exp2}, linea {self.exp2.linea}, columna {self.exp2.columna}')

        elif self.operador == Operador.DIV:
            if tipo_exp1 == Tipos.INT64 and tipo_exp2 == Tipos.INT64:
                    return self.exp1.getValor(driver, ts) / self.exp2.getValor(driver, ts)
            elif tipo_exp1 == Tipos.FLOAT64 and tipo_exp2 == Tipos.FLOAT64:
                    return self.exp1.getValor(driver, ts) / self.exp2.getValor(driver, ts)
            else:
                driver.append(f'Error Semantico, No se pueden dividir {tipo_exp1} con {tipo_exp2}, linea {self.exp2.linea}, columna {self.exp2.columna}')
                raise Exception(f'Error Semantico, No se pueden dividir {tipo_exp1} con {tipo_exp2}, linea {self.exp2.linea}, columna {self.exp2.columna}')

        elif self.operador == Operador.POTENCIA:
            if tipo_exp1 == Tipos.INT64 and tipo_exp2 == Tipos.INT64:
                    return self.exp1.getValor(driver, ts) ** self.exp2.getValor(driver, ts)
            elif tipo_exp1 == Tipos.FLOAT64 and tipo_exp2 == Tipos.FLOAT64:
                    return self.exp1.getValor(driver, ts) ** self.exp2.getValor(driver, ts)
            else:
                driver.append(f'Error Semantico, No se pueden elevar {tipo_exp1} con {tipo_exp2}, linea {self.exp2.linea}, columna {self.exp2.columna}')
                raise Exception(f'Error Semantico, No se pueden elevar {tipo_exp1} con {tipo_exp2}, linea {self.exp2.linea}, columna {self.exp2.columna}')

        elif self.operador == Operador.MODULO:
            if tipo_exp1 == Tipos.INT64 and tipo_exp2 == Tipos.INT64:
                    return self.exp1.getValor(driver, ts) % self.exp2.getValor(driver, ts)
            elif tipo_exp1 == Tipos.FLOAT64 and tipo_exp2 == Tipos.FLOAT64:
                    return self.exp1.getValor(driver, ts) % self.exp2.getValor(driver, ts)
            else:
                driver.append(f'Error Semantico, No se pueden operar modulo {tipo_exp1} con {tipo_exp2}, linea {self.exp2.linea}, columna {self.exp2.columna}')
                raise Exception(f'Error Semantico, No se pueden operar modulo {tipo_exp1} con {tipo_exp2}, linea {self.exp2.linea}, columna {self.exp2.columna}')

        else:
                driver.append(f'Error Semantico, La operacion {self.operador} no es soportado, linea {self.exp2.linea}, columna {self.exp2.columna}')
                raise Exception(f'Error Semantico, La operacion {self.operador} no es soportado, linea {self.exp2.linea}, columna {self.exp2.columna}')