# 3. Sucessor e Antecessor de um Número
# Crie um programa que leia um número inteiro e imprima seu sucessor e seu antecessor.
# Dica: Crie três variáveis: num1 (para o número digitado), antecessor (num1 - 1) e sucessor (num1 + 1).

num = int(input("Digite um número inteiro:"))
sucessor = num+1
antecessor = num-1
print ("\nVocê digitou:",num,"\nSeu sucessor é:",sucessor,"\nSeu antecessor é:",antecessor)
