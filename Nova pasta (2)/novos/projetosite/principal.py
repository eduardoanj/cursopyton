from flask import Flask, render_template, request

app = Flask

p_nome = 'HOTS- Heroes of the Storm'

@app.route('/')
def princ():
    return ('index.html')




app.run()    