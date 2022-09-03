import traceback
from flask import Flask, render_template, request
from flask_cors import CORS
from Analizador.parser import parser, getErrores
from Interpreter.TablaSimbolos.TablaSimbolos import TablaSimbolos
from Interpreter.Driver.Driver import Driver
from Interpreter.AST.ast import Ast
from Interpreter.Instrucciones.Metodo import Metodo
from Interpreter.Expresiones.LlamadaFuncion import LlamadaFuncion

app = Flask(__name__)
CORS(app)

error = []
simbs = []

@app.route('/', methods = ['GET'])
def home():
    return 'API FUNCIONA'


@app.route('/api/interpretar', methods=['POST'])
def interpretar():
    error = []

    if request.method == 'POST':
        data = request.json
        print(data)

        ts = TablaSimbolos(None, 'Global')
        driver = Driver()
        
        ast: Ast = parser.parse(data.get('instrucciones'))
        error = getErrores()

        try:
            ast.ejecutar(driver, ts, error)
        except Exception as d:
            if type(d.args[0]) == dict:
                error.append(d.args[0])
            pass

        temp = ts
        while temp != None:
            simbs.append({"ambito": ts.env, "variables": ts.tabla, "funciones":ts.tablaFunciones})
            temp = temp.anterior

        if driver.console == 'None' or driver.console == '':
            driver.console = "La entrada tiene errores sintacticos."

        return {
            'resultado': driver.console
        }

@app.route('/api/errores', methods=['POST'])
def errores():
    if request.method == 'POST':
        return {'errores': errores}

@app.route('/api/simbolos', methods=['POST'])
def simbolos():
    if request.method == 'POST':
        return {'simbolos': errores}

if __name__ == '__main__':
    app.run(host= '0.0.0.0')
    app.run(debug=True)