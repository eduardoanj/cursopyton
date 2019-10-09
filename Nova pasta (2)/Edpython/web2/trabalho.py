from flask import Flask, render_template, request, redirect

pagina_nome = 'Bom dia'

app = Flask (__name__)
@app.route('/')
def inicio():
    return render_template('index.html', pagina_nome= pagina_nome)
#a porta pela internet é a 80. se colocar dentro dos parenteses port=80 do app.run fica padrão para internet, caso eu libere a porta no firewall o computador ficará vulneravel para acessa-lo 
app.run()  


