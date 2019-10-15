from flask import Flask, render_template, redirect, Request


nome_de_la_page = "Nome da pagina"

app = Flask(__name__)

@app.route('/')
def layout():
    return render_template('layout.html', nome_de_la_page="Nome da pagina")

app.run()    
