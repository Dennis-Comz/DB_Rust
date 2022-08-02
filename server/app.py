from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from Analizador.parser import parser

app = Flask(__name__)
CORS(app)

@app.route('/', methods = ['GET'])
def home():
    return 'API FUNCIONA'

@app.route('/api/interpretar', methods=['POST'])
def interpretar():
    if request.method == 'POST':
        result = parser.parse('2 * 3 + 4 * (5 - 4) / 23')
        return {'resultado': result}

if __name__ == '__main__':
    app.run(host= '0.0.0.0')
    app.run(debug=True)