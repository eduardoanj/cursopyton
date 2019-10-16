from flask import Flask, render_template

nome_pagina = 'MusicBox'

app = Flask(__name__)

@app.route('/')
def layout():
    return render_template('index.html')

@app.route('/juntese')
def junte_se():
    return render_template('junte-se_.html', nome_pagina=nome_pagina)    




app.run()    