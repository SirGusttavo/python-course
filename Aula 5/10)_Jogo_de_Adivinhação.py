# 10. Jogo de Adivinhação: 
# Faça um programa que simule um jogo de adivinhação, onde o computador gera um número aleatório e o usuário tenta adivinhar qual é.

while(1):
    import random
    computador = random.randint(0,5)
    numero = int(input("Tente adivinhar o número que a máquina está pensando, digite um número de 0 a 5: "))
    if numero == computador:
        print ("Parabéns! Você acertou o número.")
    elif numero > 5 or numero <0:
        print ("Número inválido!") 
    else:
        print ("Você errou! O número escolhido pelo computador era", computador)