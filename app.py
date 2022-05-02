from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Receba! Obrigado meu Deus!"

if __name__ == '__main__':
    app.run()