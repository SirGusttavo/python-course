# 3. Par ou Ímpar: 
# Escreva um programa em Python que recebe um inteiro e diga se é par ou impar.

numero = int(input("Digite um número: "))
par = numero % 2
if par == 0:
    print("O número digitado é um número par!")
else:
    print("O número digitado é um número ímpar!") 