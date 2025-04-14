# 1. Manipulação de Strings
# Crie um programa que leia o nome completo de uma pessoa e mostre:

# O nome com todas as letras maiúsculas.
# O nome com todas as letras minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.

NomeCompleto = str(input('Digite seu nome completo:'))
Nome = NomeCompleto.upper()
print ('Seu nome agora é:',Nome)
Nome = NomeCompleto.lower()
print ('Seu nome agora é:',Nome)
Nome = len(NomeCompleto.replace(" ",""))
print ('A quantidade de letras do seu nome completo é:',Nome)
Nome = NomeCompleto.split()[0]
Nome = len(NomeCompleto.split()[0])
print ('A quantidade de letras do seu primeiro nome é:',Nome)