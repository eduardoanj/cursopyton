from flask import Flask, render_template, request



app = Flask(__name__)


p_nome = 'HOTS- Heroes of the Storm'

titulo_pagina = 'HOTS FLAGS'

@app.route('/')
def princ():
    return render_template('index.html')

@app.route('/intro')
def intro():
    return render_template('intro.html')




app.run()    