from flask import Flask, render_template, request, redirect
from alunos import Alunos

pagina_nome = 'Lista Alunos'
aluno1 = Alunos('Eduardo', 'Anjos', 4732097328)
aluno2 = Alunos('Angus', 'Young', 4732097328)
aluno3 = Alunos('Michael', 'Jackson', 92389348)
aluno4 = Alunos('Robert', 'Plant', 57984983)
aluno5 = Alunos('Kerry', 'King', 579494039)
aluno6 = Alunos('Dalai', 'Lama', 948494845)
aluno7 = Alunos('Sidarta', 'Gautama', 83943849)
aluno8 = Alunos('Charlie', 'Chaplin', 893483948)

lista_alunos = [aluno1, aluno2, aluno3, aluno4, aluno5, aluno6, aluno7, aluno8]
#quanto mais variaveis forem adcionadas maior a lista
app = Flask(__name__)
@app.route('/')
def inicio():
    return render_template('index.html', pagina_nome = pagina_nome, lista=lista_alunos)



#app.route é o endereço, se colocar no navegador vai acessar
@app.route('/novo')
def novo():
    return render_template('novo.html')
#o app.route é do tipo get, que apenas envia os padrões mas não o salva
@app.route('/aluno_salvar', methods=['POST'])
def salvar():
    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    telefone = request.form['telefone']
    novo_aluno = Alunos(nome, sobrenome, telefone)
    lista_alunos.append(novo_aluno)
    return redirect('/')
#importa do flask(primeira linha) o redirect, faz com que retorne para determinada página    
app.run()




'''print('='*50)

print(aluno1.nome_completo())

print('='*50)'''