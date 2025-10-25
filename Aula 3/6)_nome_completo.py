# 6. Nome Completo
# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite seu nome completo: '))
separador = nome.split()
primeiro = separador [0]
print ('Seu primeiro nome é', primeiro)
ultimo = separador [-1]
print ('Seu último nome é', ultimo)
