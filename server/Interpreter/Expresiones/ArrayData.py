from Interpreter.TablaSimbolos.Arreglo import Arreglo
from Interpreter.Expresiones.Expresion import Expresion
from server.Interpreter.TablaSimbolos.Tipos import Tipos

class ArrayData(Expresion):
    def __init__(self, listaExpresiones):
        self.listaExpresiones = listaExpresiones
        self.valores = []

    def getTipo(self, driver, ts, errores):
        tipo = any
        expresionesCompiladas = []

        #Compilar Expresiones, obtener el tamaño de cada dimension y validar congruencia de tipos
        for i in range(0, len(self.listaExpresiones)):
            expresion = self.listaExpresiones[i]
            tipoExpresion = expresion.getTipo(driver, ts, errores)
            valorExpresion = expresion.getValor(driver, ts, errores)

            if i == 0:
                tipo = tipoExpresion
                expresionesCompiladas.append(valorExpresion)
            else:
                if tipo != tipoExpresion:
                    #ERROR
                    pass
                else:
                    expresionesCompiladas.append(valorExpresion)

        #ACA SE CREA LA DATA
        listaDimensiones = []
        self.valores = []
        listaDimensiones.append(len(expresionesCompiladas)) #Tamaño de la primer dimension
        tipoFinal = any

        for i in range(0, len(expresionesCompiladas)):
            expresionCompilada = expresionesCompiladas[i]
            tipoExpresion = expresionCompilada.getTipo(driver, ts, errores)
            valorExpresion = expresionCompilada.getValor(driver, ts, errores)

            if tipoExpresion != Tipos.ARRAY:
                tipoFinal = tipoExpresion
                self.valores.append(valorExpresion)
                continue
            else:
                tipoInstancia = valorExpresion.getTipo(driver, ts, errores)
                valorInstancia = valorExpresion.getValor(driver, ts, errores)
                if i == 0:
                    tipoFinal = tipoInstancia
                    listaDimensiones.extend(len(valorInstancia))
                else:
                    if tipoExpresion != tipoFinal:
                        #error
                        pass
                self.valores.append(valorExpresion)

        return tipoFinal

    def getValor(self, driver, ts, errores):
        return self.valores