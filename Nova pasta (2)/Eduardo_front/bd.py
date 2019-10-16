from flask import Flask, render_template

nome_pagina = 'MusicBox'

app = Flask(__name__)

@app.route('/')
def layout():
    return render_template('layout.html')




app.run()    