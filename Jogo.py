import random

import tkinter as tk

janela = tk.Tk()
janela.geometry("400x300")
janela.title('Pedra,Papel e Tesoura Jogo')


USUARIO_PONTOS = 0
COMP_PONTOS = 0
USUARIO_ESCOLHA = ""
COMP_ESCOLHA = ""


def escolha_de_numero(escolha):
    opcoes = {'pedra':0,'papel':1,'tesoura':2}
    return opcoes[escolha]


def numero_de_escolha(numero):
    opcoes = {1:'pedra',2:'papel',3:'tesoura'}
    return opcoes[numero]


def escolha_aleatoria_computador():
    return random.choice(['pedra','papel','tesoura'])


def resultado(escolha_usuario,escolha_comp):
    global USUARIO_PONTOS
    global COMP_PONTOS
    usuario = escolha_de_numero(escolha_usuario)
    comp = escolha_de_numero(escolha_comp)
    if usuario == comp:
        print("Empate")
    elif (usuario - comp) % 3 == 1:
        USUARIO_PONTOS +=1
        print("Você Venceu")
    else:
        COMP_PONTOS += 1
        print("Computador Venceu")
    text_area = tk.Text(master=janela,height=12,width=30, bg="#FFFF99")
    text_area.grid(column=0,row=4)
    resposta = f'Sua escolha: {USUARIO_ESCOLHA}\nComputador escolha: {COMP_ESCOLHA}\nsua pontuação:{USUARIO_PONTOS}\nComputador Pontuação:{COMP_PONTOS}'
    text_area.insert(tk.END,resposta)


def pedra():
    global USUARIO_ESCOLHA
    global COMP_ESCOLHA
    USUARIO_ESCOLHA = 'pedra'
    COMP_ESCOLHA = escolha_aleatoria_computador()
    resultado(USUARIO_ESCOLHA,COMP_ESCOLHA)


def papel():
    global USUARIO_ESCOLHA
    global COMP_ESCOLHA
    USUARIO_ESCOLHA = 'papel'
    COMP_ESCOLHA = escolha_aleatoria_computador()
    resultado(USUARIO_ESCOLHA,COMP_ESCOLHA)


def tesoura():
    global USUARIO_ESCOLHA
    global COMP_ESCOLHA
    USUARIO_ESCOLHA = 'tesoura'
    COMP_ESCOLHA = escolha_aleatoria_computador()
    resultado(USUARIO_ESCOLHA,COMP_ESCOLHA)

botao1 = tk.Button(text="    Pedra     ",bg='red',command=pedra)
botao1.grid(column=0,row=1)
botao2 = tk.Button(text="    Papel     ",bg='blue',command=papel)
botao2.grid(column=0,row=2)
botao3 = tk.Button(text="    Tesoura     ",bg='green',command=tesoura)
botao3.grid(column=0,row=3)

janela.mainloop()






