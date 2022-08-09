from Interpreter.Expresiones.Operaciones.OperacionRelacional import OperacionRelacional, Operador, getOperacion
from Interpreter.TablaSimbolos.Tipos import Tipos, definirTipo

class Relacionales(OperacionRelacional):

    def getTipo(self, driver, ts):
        value = self.getValor(driver, ts)
        return definirTipo(value)

    def getValor(self, driver, ts):
        tipo_exp1 = self.exp1.getTipo(driver, ts)
        tipo_exp2 = self.exp2.getTipo(driver, ts)

        if self.operador == Operador.IGUAL_IGUAL:
            if tipo_exp1 == Tipos.INT64 and tipo_exp2 == Tipos.INT64:
                return self.exp1.getValor(driver, ts) == self.exp2.getValor(driver,ts)
            elif tipo_exp1 == Tipos.FLOAT64 and tipo_exp2 == Tipos.FLOAT64:
                return self.exp1.getValor(driver, ts) == self.exp2.getValor(driver,ts)
            elif tipo_exp1 == Tipos.BOOLEAN and tipo_exp2 == Tipos.BOOLEAN:
                return self.exp1.getValor(driver, ts) == self.exp2.getValor(driver,ts)
            elif tipo_exp1 == Tipos.STR_BUFFER and tipo_exp2 == Tipos.STR_BUFFER:
                return self.exp1.getValor(driver, ts) == self.exp2.getValor(driver,ts)
            elif tipo_exp1 == Tipos.STR_POINTER and tipo_exp2 == Tipos.STR_POINTER:
                return self.exp1.getValor(driver, ts) == self.exp2.getValor(driver,ts)
            elif tipo_exp1 == Tipos.STR_BUFFER and tipo_exp2 == Tipos.STR_POINTER:
                return self.exp1.getValor(driver, ts) == self.exp2.getValor(driver,ts)
            elif tipo_exp1 == Tipos.STR_POINTER and tipo_exp2 == Tipos.STR_BUFFER:
                return self.exp1.getValor(driver, ts) == self.exp2.getValor(driver,ts)
            else:
                print(f'No se pueden comparar {tipo_exp1} con {tipo_exp2}', self.exp2.linea, self.exp2.columna)
        elif self.operador == Operador.NO_IGUAL:
            if tipo_exp1 == Tipos.INT64 and tipo_exp2 == Tipos.INT64:
                return self.exp1.getValor(driver, ts) != self.exp2.getValor(driver,ts)
            elif tipo_exp1 == Tipos.FLOAT64 and tipo_exp2 == Tipos.FLOAT64:
                return self.exp1.getValor(driver, ts) != self.exp2.getValor(driver,ts)
            elif tipo_exp1 == Tipos.BOOLEAN and tipo_exp2 == Tipos.BOOLEAN:
                return self.exp1.getValor(driver, ts) != self.exp2.getValor(driver,ts)
            elif tipo_exp1 == Tipos.STR_BUFFER and tipo_exp2 == Tipos.STR_BUFFER:
                return self.exp1.getValor(driver, ts) != self.exp2.getValor(driver,ts)
            elif tipo_exp1 == Tipos.STR_POINTER and tipo_exp2 == Tipos.STR_POINTER:
                return self.exp1.getValor(driver, ts) != self.exp2.getValor(driver,ts)
            elif tipo_exp1 == Tipos.STR_BUFFER and tipo_exp2 == Tipos.STR_POINTER:
                return self.exp1.getValor(driver, ts) != self.exp2.getValor(driver,ts)
            elif tipo_exp1 == Tipos.STR_POINTER and tipo_exp2 == Tipos.STR_BUFFER:
                return self.exp1.getValor(driver, ts) != self.exp2.getValor(driver,ts)
            else:
                print(f'No se pueden comparar {tipo_exp1} con {tipo_exp2}', self.exp2.linea, self.exp2.columna)
        
        elif self.operador == Operador.MAYOR:
            if tipo_exp1 == Tipos.INT64 and tipo_exp2 == Tipos.INT64:
                return self.exp1.getValor(driver, ts) > self.exp2.getValor(driver,ts)
            elif tipo_exp1 == Tipos.FLOAT64 and tipo_exp2 == Tipos.FLOAT64:
                return self.exp1.getValor(driver, ts) > self.exp2.getValor(driver,ts)
            elif tipo_exp1 == Tipos.BOOLEAN and tipo_exp2 == Tipos.BOOLEAN:
                return self.exp1.getValor(driver, ts) > self.exp2.getValor(driver,ts)
            elif tipo_exp1 == Tipos.STR_BUFFER and tipo_exp2 == Tipos.STR_BUFFER:
                return self.exp1.getValor(driver, ts) > self.exp2.getValor(driver,ts)
            elif tipo_exp1 == Tipos.STR_POINTER and tipo_exp2 == Tipos.STR_POINTER:
                return self.exp1.getValor(driver, ts) > self.exp2.getValor(driver,ts)
            elif tipo_exp1 == Tipos.STR_BUFFER and tipo_exp2 == Tipos.STR_POINTER:
                return self.exp1.getValor(driver, ts) > self.exp2.getValor(driver,ts)
            elif tipo_exp1 == Tipos.STR_POINTER and tipo_exp2 == Tipos.STR_BUFFER:
                return self.exp1.getValor(driver, ts) > self.exp2.getValor(driver,ts)
            else:
                print(f'No se pueden comparar {tipo_exp1} con {tipo_exp2}', self.exp2.linea, self.exp2.columna)
        
        elif self.operador == Operador.MENOR:
            if tipo_exp1 == Tipos.INT64 and tipo_exp2 == Tipos.INT64:
                return self.exp1.getValor(driver, ts) < self.exp2.getValor(driver,ts)
            elif tipo_exp1 == Tipos.FLOAT64 and tipo_exp2 == Tipos.FLOAT64:
                return self.exp1.getValor(driver, ts) < self.exp2.getValor(driver,ts)
            elif tipo_exp1 == Tipos.BOOLEAN and tipo_exp2 == Tipos.BOOLEAN:
                return self.exp1.getValor(driver, ts) < self.exp2.getValor(driver,ts)
            elif tipo_exp1 == Tipos.STR_BUFFER and tipo_exp2 == Tipos.STR_BUFFER:
                return self.exp1.getValor(driver, ts) < self.exp2.getValor(driver,ts)
            elif tipo_exp1 == Tipos.STR_POINTER and tipo_exp2 == Tipos.STR_POINTER:
                return self.exp1.getValor(driver, ts) < self.exp2.getValor(driver,ts)
            elif tipo_exp1 == Tipos.STR_BUFFER and tipo_exp2 == Tipos.STR_POINTER:
                return self.exp1.getValor(driver, ts) < self.exp2.getValor(driver,ts)
            elif tipo_exp1 == Tipos.STR_POINTER and tipo_exp2 == Tipos.STR_BUFFER:
                return self.exp1.getValor(driver, ts) < self.exp2.getValor(driver,ts)
            else:
                print(f'No se pueden comparar {tipo_exp1} con {tipo_exp2}', self.exp2.linea, self.exp2.columna)
        
        elif self.operador == Operador.MAYOR_IGUAL:
            if tipo_exp1 == Tipos.INT64 and tipo_exp2 == Tipos.INT64:
                return self.exp1.getValor(driver, ts) >= self.exp2.getValor(driver,ts)
            elif tipo_exp1 == Tipos.FLOAT64 and tipo_exp2 == Tipos.FLOAT64:
                return self.exp1.getValor(driver, ts) >= self.exp2.getValor(driver,ts)
            elif tipo_exp1 == Tipos.BOOLEAN and tipo_exp2 == Tipos.BOOLEAN:
                return self.exp1.getValor(driver, ts) >= self.exp2.getValor(driver,ts)
            elif tipo_exp1 == Tipos.STR_BUFFER and tipo_exp2 == Tipos.STR_BUFFER:
                return self.exp1.getValor(driver, ts) >= self.exp2.getValor(driver,ts)
            elif tipo_exp1 == Tipos.STR_POINTER and tipo_exp2 == Tipos.STR_POINTER:
                return self.exp1.getValor(driver, ts) >= self.exp2.getValor(driver,ts)
            elif tipo_exp1 == Tipos.STR_BUFFER and tipo_exp2 == Tipos.STR_POINTER:
                return self.exp1.getValor(driver, ts) >= self.exp2.getValor(driver,ts)
            elif tipo_exp1 == Tipos.STR_POINTER and tipo_exp2 == Tipos.STR_BUFFER:
                return self.exp1.getValor(driver, ts) >= self.exp2.getValor(driver,ts)
            else:
                print(f'No se pueden comparar {tipo_exp1} con {tipo_exp2}', self.exp2.linea, self.exp2.columna)

        elif self.operador == Operador.MENOR_IGUAL:
            if tipo_exp1 == Tipos.INT64 and tipo_exp2 == Tipos.INT64:
                return self.exp1.getValor(driver, ts) <= self.exp2.getValor(driver,ts)
            elif tipo_exp1 == Tipos.FLOAT64 and tipo_exp2 == Tipos.FLOAT64:
                return self.exp1.getValor(driver, ts) <= self.exp2.getValor(driver,ts)
            elif tipo_exp1 == Tipos.BOOLEAN and tipo_exp2 == Tipos.BOOLEAN:
                return self.exp1.getValor(driver, ts) <= self.exp2.getValor(driver,ts)
            elif tipo_exp1 == Tipos.STR_BUFFER and tipo_exp2 == Tipos.STR_BUFFER:
                return self.exp1.getValor(driver, ts) <= self.exp2.getValor(driver,ts)
            elif tipo_exp1 == Tipos.STR_POINTER and tipo_exp2 == Tipos.STR_POINTER:
                return self.exp1.getValor(driver, ts) <= self.exp2.getValor(driver,ts)
            elif tipo_exp1 == Tipos.STR_BUFFER and tipo_exp2 == Tipos.STR_POINTER:
                return self.exp1.getValor(driver, ts) <= self.exp2.getValor(driver,ts)
            elif tipo_exp1 == Tipos.STR_POINTER and tipo_exp2 == Tipos.STR_BUFFER:
                return self.exp1.getValor(driver, ts) <= self.exp2.getValor(driver,ts)
            else:
                print(f'No se pueden comparar {tipo_exp1} con {tipo_exp2}', self.exp2.linea, self.exp2.columna)
        
        else:
            print(f'La operacion {self.operador} no es soportado')