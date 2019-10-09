from flask import Flask, render_template
from aluno import Alunos

pagina_nome = 'Lista Alunos'
 al1 = Alunos('asdasd', 4564646)
 lista_alunos = [aluno1]

app = Flask(__name__)
@app.route('/')
def inicio():
    return 'asdasda' #render_template('index.html', pagina_nome = pagina_nome, lista=lista_alunos)
app.run()