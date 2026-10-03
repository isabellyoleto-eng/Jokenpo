from flask import Flask, request, jsonify, render_template

from jogo import jogar


app = Flask(__name__)


@app.route("/")
def inicio():

    return render_template("index.html")


@app.route("/jogar", methods=["POST"])
def jogar_partida():

    dados = request.get_json()

    escolha = dados["escolha"]

    resultado = jogar(escolha)

    return jsonify(resultado)


if __name__ == "__main__":

    app.run(debug=True)                                                