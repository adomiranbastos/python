#Flask é uma (Framawork) estrutura Python para construir um aplicativo da web.

""" 
app.route define o URL e a função a ser executada para cada URL. 

Quando apenas '/' é especificado no URL, presume-se que seja a página inicial. 
Este aplicativo da web exibirá o texto '<h1> BEM-VINDO para Minha página inicial </h1> ' 
no estilo do cabeçalho 1. 

Quando o URL contém um nome no URL, o nome do URL é analisado para ser usado 
na função que atende a página da web. Isso é conhecido como "dinâmico página da web. " 

Quando admin é específico no URL, o admin () irá executar para 
redirecionar a página para mostrar a página inicial. 

Consulte as imagens abaixo para uma visão de como cada página. 
"""  

# Import packages
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
  return "<h1> BEM-VINDO à minha página inicial</h1>"

@app.route("/<name>")
def user(name):
  return f"<h3>Olá, prazer em conhecê-lo {name}!</h3>"

@app.route("/admin")
def admin():
  return redirect(url_for("home"))

if __name__ == "__main__":
  app.run()