import random
from math import sqrt
from time import sleep
import funcoes

#funcões do primeiro menu:

def SomaNumeros(a, b):
    return a + b

def Multiplicacao(a, b):
    return a * b

def Divisao(a, b):
    return a // b      

def subtracao(a, b):
    return a - b

def raizquadrada(a):
    return sqrt(a)

def ErroMensage(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Digite apenas numeros inteiros.")


def joguinho():
    print("Digite 90 para sair")
    pc = random.randint(1, 10)
    tentativas = 0
    dificil = input("Quer jogar o modo dificil? (S/N)").upper()
    pcdificil = random.randint(1, 50)
    while True:
        
        if dificil == "S":
            while True: 
                jogador = ErroMensage("O computador pensou em um numero entre 1 e 50 de seu palpite!:  ")
                tentativas += 1
                if jogador == 90:
                    print("Saindo....")
                    sleep(0.5)
                    break
                elif jogador == pcdificil:
                    print(f"Você ganhou com {tentativas} tentativas!")
                    sleep(0.5)
                    break
                elif jogador > pcdificil:
                    print("Jogue um numero menor....")
                    sleep(0.3)
                elif jogador < pcdificil:
                    print("Jogue um numero maior.....")
                    sleep(0.3)
        else:
            
            jogador = ErroMensage("O computador pensou em um numero entre 1 e 10 de seu palpite!: ")
            tentativas += 1 
            if jogador == 90:
                print("Saindo...") 
                sleep(0.3)
                break

            if jogador == pc:
                print(f"Você ganhou em {tentativas} tentativas!")
                sleep(1)
                break
            if jogador > pc:
                print("Jogue um numero menor....")
                sleep(0.3)
            else:
                print("Jogue um numero maior.....") 
                sleep(0.3)
# ==========================================
#fuções do segundo menu: 

def JogoFacil():
    print("Você selecionou o modo de jogo facil, a soma!")
    numero1 = random.randint(10, 50)
    numero2 = random.randint(20, 60)
    resultado = funcoes.SomaNumeros(numero1, numero2)

    contador = 0
    while True:
        contador += 1
        tentativa = funcoes.ErroMensage(f"quanto é {numero1} + {numero2}? :   ")
        if tentativa == resultado:
            print(f"Parabens! voce acertou com {contador} tentativas! ")
            sleep(0.5)
            break
        else:
            print("Voce errou......") 
            sleep(0.5)   

def JogoMedio():
    print("Você escolheu o modo médio de subtração! ")
    numero1 = random.randint(10, 20)
    numero2 = random.randint(5, 10)
    contador = 0
    resultado = funcoes.subtracao(numero1, numero2)
    while True:
        contador += 1
        tentativa = funcoes.ErroMensage(f"quanto é {numero1} - {numero2} ?  :  ")
        if tentativa == resultado:
            print(f"Parabens! voce passou com {contador} tentativas! ")
            sleep(0.5)
            break
        else:
            print("Você errou, tente novamente...")
            sleep(0.3)

def JogoDificil():
    print("Você escolheu a opção dificil!")
    sleep(0.3)
    numero1 = random.randint(10, 20)
    numero2 = random.randint(15, 30)
    contador = 0
    resultado = round(numero1 / numero2, 1) 
    while True:
        tentativa = float(input(f"quanto é {numero1} dividido por {numero2}? :  "))
        contador += 1
        if tentativa == resultado:
            print(f"Parabens voce conseguiu com {contador} tentativa(s)! ")
            sleep(0.5)
            break
        else:
            print("Tente novamente........")

def jogoMuitoDificil():
    numero1 = random.randint(20, 100)
    numero2 = random.randint(30, 150)
    contador = 0
    resultado = funcoes.Multiplicacao(numero1, numero2)
    while True:
        contador += 1
        tentativa = funcoes.ErroMensage(f"Quando é {numero1:.2f} vezes {numero2:.2f}?   :   ")
        if tentativa == resultado:
            print(f"Parabens! voce conseguiu com {contador} tentativas! ")
            sleep(0.5)
            break
        else:
            print("Você errou.... tente novamente..")
            sleep(0.3)
