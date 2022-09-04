import traceback
from flask import Flask, render_template, request
from flask_cors import CORS
from Analizador.parser import parser, getErrores
from Interpreter.TablaSimbolos.TablaSimbolos import TablaSimbolos
from Interpreter.Driver.Driver import Driver
from Interpreter.AST.ast import Ast
from static import error, simbs

app = Flask(__name__)
CORS(app)


@app.route('/', methods = ['GET'])
def home():
    return 'API FUNCIONA'


@app.route('/api/interpretar', methods=['POST'])
def interpretar():
    if request.method == 'POST':
        data = request.json
        print(data)

        ts = TablaSimbolos(None, 'Global')
        driver = Driver()
        
        ast: Ast = parser.parse(data.get('instrucciones'))
        arr = getErrores()
        for i in arr:
            error.append(i)

        try:
            ast.ejecutar(driver, ts, error)
        except Exception as d:
            if type(d.args[0]) == dict:
                error.append(d.args[0])
            pass

        simbs.append(ts)

        if driver.console == 'None' or driver.console == '':
            driver.console = "La entrada tiene errores sintacticos."

        return {
            'resultado': driver.console
        }

@app.route('/api/errores', methods=['POST'])
def errores():
    if request.method == 'POST':
        temp = error
        return {'errores': error}

@app.route('/api/simbolos', methods=['POST'])
def simbolos():
    if request.method == 'POST':
        salida = []
        for s in simbs:
            for val in s.tabla:
                salida.append({"id":val, "tipo": s.tabla[val].tipo.name, "simbolo":"Variable", "ambito":s.env})
            for fun in s.tablaFunciones:
                salida.append({"id":fun, "tipo": s.tablaFunciones[fun].tipo.name, "simbolo":"Funcion", "ambito":s.env})
                print(fun)
        return {'simbolos': salida}

if __name__ == '__main__':
    app.run(host= '0.0.0.0')
    app.run(debug=True)