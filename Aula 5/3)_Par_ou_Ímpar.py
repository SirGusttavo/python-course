# 3. Par ou Ímpar: 
# Faça um programa que verifique se um número é par ou ímpar.

numero = int(input("Digite um número: "))
par = numero % 2
if par == 0:
    print("O número digitado é um número par!")
else:
    print("O número digitado é um número ímpar!") 