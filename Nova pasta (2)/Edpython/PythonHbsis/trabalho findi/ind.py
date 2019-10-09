from flask import Flask, render_template, request, redirect
from classes import Investimento

titulo_pagina = 'Hpinvestimentos.org'

app = Flask(__name__)

lista_invest = []

@app.route('/')
def princ():
    return render_template('index.html')

@app.route('/investimentos')
def cat():
    return render_template('investimentos.html', titulo_pagina= 'investimentos.org', lista=lista_invest)

@app.route('/salvar', methods=['POST'])
def salvar():
    categoria = request.form['categoria']
    tipo = request.form['tipo']
    aporte = request.form['aporte']
    rentabilidade = request.form['rentabilidade']
    novo_investimento = Investimento(categoria, tipo, aporte, rentabilidade)
    lista_invest.append(novo_investimento)
    return render_template('lista_inv.html')   



app.run()    