import secrets
from flask import Flask, request, render_template, flash

import tverdade

app = Flask(__name__)
app.secret_key = secrets.token_hex()

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        expressao = request.form['expressao']
        expressao_valida = tverdade.verificar_expressao(expressao) 
        if expressao_valida:
            variaveis = tverdade.extrair_variaveis(expressao)
            combinacoes = tverdade.gerar_combinacoes(variaveis)
            resultados = tverdade.analisar_expressao(expressao, combinacoes)
            response = {
                "expressao": expressao,
                "variaveis": variaveis,
                "combinacoes": combinacoes,
                "resultados": resultados
            }
            return render_template('index.html', response=response)
        else:
            erro = 'Expressão não é válida, tente novamente.'
            flash(erro)

    return render_template('index.html')

@app.route("/sobre")
def about():
    return "about"