from flask import Flask, render_template, request
from flask_cors import CORS
from Analizador.parser import parser
from Interpreter.TablaSimbolos.TablaSimbolos import TablaSimbolos
from Interpreter.Driver import Driver
from Interpreter.AST.ast import Ast

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
        ast: Ast = parser.parse(data.get('instrucciones'))

        ts = TablaSimbolos(None, 'Global')
        driver = Driver.Driver()

        ast.ejecutar(driver, ts)

        return {
            'resultado': driver.console
        }

if __name__ == '__main__':
    app.run(host= '0.0.0.0')
    app.run(debug=True)