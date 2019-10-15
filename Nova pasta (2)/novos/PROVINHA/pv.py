from flask import Flask, render_template, request, redirect
from cliente import Cliente
import MySQLdb

def listar_clientes():
    cliente1 = Cliente()
    cliente1.id = 1
    cliente1.nome = 'Luisinho'
    cliente1.cpf = '082.730.329-73'
    cliente1.nascimento = '15/04/1998'
    lista = [cliente1]
    return lista

def listar_clientes_db():
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae04", passwd="lendas19", database="zuplae04")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM Cliente")
    lista_cliente = []
    for i in cursor.fetchall():
        cliente2 = Cliente()
        cliente2.id = i[0]
        cliente2.nome = i[1]
        cliente2.cpf = i[2]
        cliente2.nascimento = i[3]
        lista_cliente.append(cliente2)
    conexao.close()
    return lista_cliente

def salvar_cliente_db(nome, cpf,dt_nasc):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae04", passwd="lendas19", database="zuplae04")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO Cliente (nome,cpf,data_nascimento)" + 
    " VALUES ('{}', '{}', '{}')".format(nome,cpf,dt_nasc))
    conexao.commit()

def deletar_cliente(id):
    conexao = MySQLdb.connect(host="mysql.zuplae.com", user="zuplae04", passwd="lendas19", database="zuplae04")
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM Cliente WHERE id={}".format(id))
    conexao.commit()


nome_de_la_page = "Nome da pagina"

app= Flask(__name__)
@app.route('/')
def inicio():
    return render_template('index.html', nome_de_la_page = nome_de_la_page)

@app.route('/cliente/lista')
def lista_cliente():
    lista = listar_clientes_db()
    return render_template('lista_cliente.html', nome_de_la_page = nome_de_la_page, lista = lista)

@app.route('/cliente')
def cliente():
    return render_template('cliente.html', nome_de_la_page = nome_de_la_page)

@app.route('/cliente/salvar', methods = ['POST'])
def salvar():
    nome = request.form['nome']
    cpf = request.form['cpf']
    nascimento = request.form['nascimento']
    cliente = Cliente()
    cliente.nome = nome 
    cliente.cpf = cpf
    cliente.nascimento = nascimento
    salvar_cliente_db(cliente.nome, cliente.cpf, cliente.nascimento)
    return redirect('/cliente/lista')
@app.route('/cliente/delete')
def deletar():
    id = request.args['id']
    deletar_cliente(id)
    return redirect ('/cliente/lista')

app.run()
