from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular_idade', methods=['POST'])
def calcular_idade():
    ano_nascimento = int(request.form['idade'])
    idade_calculada = 2025 - ano_nascimento
    return render_template('index.html', calcular_idade=idade_calculada)

if __name__ == '__main__':
    app.run(debug=True)