import random
from math import sqrt
from time import sleep
import funcoes
#Defs do menu principal

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
#menu de jogos, mais abaixo defs do menu de jogos       
def Jogosmatematicos():
    print("""    1 - Jogo matemático facil
    2 - Jogo matemático médio
    3 - jogo matemático dificil
    4 - Jogo matemático muito dificil
    5 - Voltar menu principal""")


def menu():
    print("""
    1 - Soma
    2 - multiplicação
    3 - divisão
    4 - subtração
    5 - raizquadrada
    6 - jogo de adivinha
    7 - troca de numeros
    8 - Jogos matematicos
    9 - sair do app""")

while True:
    try:
        num1 = int(input("Diga o primeiro número: "))
        num2 = int(input("Diga o segundo número: "))
        break
    except ValueError:
        print("Apenas números, tudo alem disso não é aceito.")


while True:
    
    menu()
    while True:
        try:
            opcao = int(input("Digite sua opção: "))
            if opcao >=1 and opcao <= 9:
                break
            else:
                print("Opção invalida, digite um numero entre 1 e 9")
        except ValueError:
            print("Apenas numeros são aceitos.")
            menu()


    if opcao == 1:
        print(f"{num1} + {num2} = {funcoes.SomaNumeros(num1, num2)}")
        sleep(0.5)

    elif opcao == 2:
        print(f"{num1} x {num2} = {funcoes.Multiplicacao(num1, num2)}")
        sleep(0.5)

    elif opcao == 3:
        if num1 == 0 or num2 ==0:
            print("Nao é possivel dividir por 0")
            sleep(0.5)
        else:
            print(f"{num1} dividido por {num2} = {funcoes.Divisao(num1, num2)}")
            sleep(0.5)

    elif opcao == 4:
        print(f"{num1} - {num2} = {funcoes.subtracao(num1, num2)}")
        sleep(0.5)

    elif opcao == 5:
        print(f"raiz quadrada de {num1} é {funcoes.raizquadrada(num1):.2f}")
        sleep(0.3)
        print(f"A raiz quadrada de {num2} é = {funcoes.raizquadrada(num2):.2f}")
        test = input("Deseja fazer raiz quadrada com mais algum numero? (S/N)").upper()
        if test == "S":
            while True:
                n = ErroMensage("Qual numero: ")
                print(f"A raiz quadrada de {n} é {funcoes.raizquadrada(n):.2f}")
                test = input("Deseja continuar? (S/N)").upper()
                if test == "N":
                    break

    elif opcao == 6:
        joguinho()

    elif opcao == 7:
        num1 = ErroMensage("Diga o novo primeiro numero: ")
        num2 = ErroMensage("Diga o novo segundo numero: ")
    
    elif opcao == 9:
        print("Saindo....")
        sleep(0.4)
        break



    elif opcao == 8:
        while True:
            Jogosmatematicos()
            while True:
                try:
                    opcao2 = ErroMensage("Digite sua dificuldade: ")
                    if opcao2 >=1 and opcao2 <=5:
                        break
                except ValueError:
                    print("Erro, tente escolher opções entre 1 e 5")

                
            if opcao2 == 1:
                funcoes.JogoFacil()

            elif opcao2 == 2:
                funcoes.JogoMedio()
            elif opcao2 == 3:
                funcoes.JogoDificil()
            elif opcao2 == 4:
                funcoes.jogoMuitoDificil()
            
            elif opcao2 == 5:
                print("Saindo...")
                sleep(0.5)
                break
            
                


    

    


