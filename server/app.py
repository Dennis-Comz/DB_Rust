import traceback
from flask import Flask, render_template, request
from flask_cors import CORS
from Analizador.parser import parser
from Interpreter.TablaSimbolos.TablaSimbolos import TablaSimbolos
from Interpreter.Driver.Driver import Driver
from Interpreter.AST.ast import Ast
from Interpreter.Instrucciones.Metodo import Metodo
from Interpreter.Expresiones.LlamadaFuncion import LlamadaFuncion

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
        # errores = parser.getErrores()
        # print(errores)

        try:
            ast.ejecutar(driver, ts)
        except: 
            traceback.print_exc()

        if driver.console == 'None':
            driver.console = "La entrada tiene errores."

        return {
            'resultado': driver.console
        }

if __name__ == '__main__':
    app.run(host= '0.0.0.0')
    app.run(debug=True)