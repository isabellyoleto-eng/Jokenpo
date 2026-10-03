import random


def jogar(escolha_jogador):

    opcoes = ["pedra", "papel", "tesoura"]

    escolha_computador = random.choice(opcoes)

    if escolha_jogador == escolha_computador:

        resultado = "Empate!"

    elif (
        (escolha_jogador == "pedra" and escolha_computador == "tesoura")
        or
        (escolha_jogador == "papel" and escolha_computador == "pedra")
        or
        (escolha_jogador == "tesoura" and escolha_computador == "papel")
    ):

        resultado = "Você ganhou!"

    else:

        resultado = "Computador ganhou!"

    return {
        "jogador": escolha_jogador,
        "computador": escolha_computador,
        "resultado": resultado
    }