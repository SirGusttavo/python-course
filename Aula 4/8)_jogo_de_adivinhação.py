# 8. Jogo de Adivinhação:
# O computador escolhe um número aleatório entre 0 e 5.
# Solicite ao usuário que tente adivinhar o número.
# Se o usuário acertar, exiba "Parabéns! Você acertou o número.". Caso contrário, exiba "Você errou. O número escolhido pelo computador era {número}".

import random

while True:
    computador = random.randint(0, 5)
    numero = int(input("Tente adivinhar o número que a máquina está pensando, digite um número de 0 a 5: "))
    
    if numero == computador:
        print("Parabéns! Você acertou o número.")
        sair = input("Deseja continuar? (s/n) ")
        if sair.lower() == "n":
            print("Fim de Jogo!")
            break
        elif sair.lower() == "s":
            print("Você escolheu continuar!")
            continue
    elif numero > 5 or numero < 0:
        print("Número inválido!") 
    else:
        print("Você errou! O número escolhido pelo computador era", computador)
    
    sair = input("Deseja continuar? (s/n) ")
    if sair.lower() == "n":
        print("Fim de Jogo!")
        break
    elif sair.lower() == "s":
        print("Você escolheu continuar!")
        continue
