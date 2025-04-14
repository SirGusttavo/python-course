#  2. Separação de Dígitos
# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

minimo = 0
maximo = 9999
numero = float(input('Digite um número de 0 a 9999:'))

unidade = numero % 10
dezena = (numero // 10) % 10
centena = (numero // 100) % 10
milhar = (numero //  1000) % 10

if minimo <= numero <= maximo:
   print("Unidade:", unidade)
   print("Dezena:", dezena)
   print("Centena:", centena)
   print("Milhar:", milhar)
else:
   print("Número inválido!")
   
   
