from Interpreter.Instrucciones.Instruccion import Instruccion
from Interpreter.Expresiones.Expresion import Expresion

class PrintLn(Instruccion):
    def __init__(self, exp: Expresion, expresiones, linea, columna):
        self.exp = exp
        self.expresiones = expresiones
        self.columna = columna
        self.linea = linea

    def ejecutar(self, driver, ts):
        try:
            cadena = str(self.exp.getValor(driver, ts))
            exps = []
            for e in self.expresiones:
                e.getTipo(driver, ts)
                exps.append(e.getValor(driver, ts))
            
            cadena = self.obtenerCadenaFinal(cadena, exps, driver)
            cadena = cadena.replace("\\n", '\n')
            cadena = cadena.replace("\\\\", '\\')
            cadena = cadena.replace("\\\"", '\"')
            cadena = cadena.replace("\\t", '\t')
            cadena = cadena.replace("\\'", '\'')
            if cadena != 'None':
                driver.append(cadena)
        except:
            pass    
    def obtenerCadenaFinal(self, cadena, arrayVals, driver):
        cadena += " "
        cads = []
        cad = ""
        contadorAbre = 0
        contadorCierra = 0
        for i in range(0, len(cadena)):
            if cadena[i] == "{":
                contadorAbre += 1
            elif cadena[i] == "}":
                contadorCierra += 1
            elif contadorAbre != 0 and contadorCierra != 0:
                if contadorAbre == contadorCierra:
                    cads.append(cad)
                    if contadorAbre % 2 == 0:
                        llava = int(contadorAbre/2)*"{"
                        llavc = int(contadorAbre/2)*"}"
                        cads.append(llava+llavc + cadena[i])
                    else:
                        if len(arrayVals) == 0:
                            driver.append(f'Error Semantico, se esperaba mas valores que los dados, linea {self.linea}, columna {self.columna}')
                            raise Exception(f'Error Semantico, se esperaba mas valores que los dados, linea {self.linea}, columna {self.columna}')
                        if contadorAbre > 1:
                            llava = int(contadorAbre/2)*"{"
                            llavc = int(contadorAbre/2)*"}"
                            cads.append(llava + str(arrayVals.pop(0)) + llavc + cadena[i])
                        else:
                            cads.append(str(arrayVals.pop(0)) + cadena[i])
                    cad = ""
                    contadorAbre = 0
                    contadorCierra = 0
                else:
                    driver.append(f'Error Semantico, falto una llave de apertura o de cierre, linea {self.linea}, columna {self.columna}')
                    raise Exception(f'Error Semantico, falto una llave de apertura o de cierre, linea {self.linea}, columna {self.columna}')
            elif contadorAbre == 0 and contadorCierra == 0:
                cad += cadena[i]
        
        if len(arrayVals) != 0:
            driver.append(f'Error Semantico, se pasaron mas argumentos de los esperados, linea {self.linea}, columna {self.columna}')
            raise Exception(f'Error Semantico, se pasaron mas argumentos de los esperados, linea {self.linea}, columna {self.columna}')
        salida = ""
        for v in cads:
            salida += v
        
        if salida != "":
            return salida
        else:
            return cadena