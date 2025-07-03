from flask import Flask, render_template, request, make_response, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    # Renderiza a página inicial com os links para votar e ver resultado
    return render_template('index.html')

@app.route("/votar", methods=['GET', 'POST'])
def votar():
    if request.method == 'GET':
        return render_template('votar.html')
    nome = request.form.get("nome") # coleta o nome digitado
    genero = request.form.get("genero")
    # Armazena o nome num cookie com validade de 5 minutos (60s x 5 = 300s)
    response = make_response(redirect(url_for('resultado', genero=genero)))
    response.set_cookie('nome', nome, max_age=300)
    
    return response

@app.route('/resultado')
def resultado():
   genero = request.args.get("genero", "não informado") # pega o gênero da URL (string de consulta)
   nome = request.cookies.get("nome", "Visitante") # tenta pegar o nome do cookie (ou "Visitante") 

   return render_template('resultado.html', genero=genero, nome=nome)