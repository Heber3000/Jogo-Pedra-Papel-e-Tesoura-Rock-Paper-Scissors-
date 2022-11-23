import random

import tkinter as tk

janela = tk.Tk()
janela.geometry("400x300")
janela.title("Pedra,Papel e Tesoura")

PONTOS_USUARIO = 0
PONTOS_COMPUTADOR = 0
ESCOLHA_USUARIO = ""
ESCOLHA_COMPUTADOR = ""


def escolha_um_numero(escolha):
    opcoes = {'pedra(rock)': 0, 'papel(paper)': 1, 'tesoura(scissors)': 2}
    return opcoes[escolha]


def numero_de_escolha(escolha):
    opcoes = {0: 'pedra(rock)', 1: 'papel(paper)', 'tesoura(scissors)': 2}
    return opcoes[escolha]


def escolha_aleatoria_do_computador():
    return random.choice(['pedra(rock)', 'papel(paper)', 'tesoura(scissors)'])


def resultado(escolha_humana, escolha_computador):
    global PONTOS_USUARIO
    global PONTOS_COMPUTADOR
    usuario = escolha_um_numero(escolha_humana)
    comp = escolha_computador(escolha_computador)
    if usuario == comp:
        print('Empate')
    elif (usuario -comp) % 3 == 1:
        print('Venceu')
        PONTOS_USUARIO += 1
    else:
        print('Computador Venceu')
        PONTOS_COMPUTADOR += 1



