# 1. Média do Aluno: 
# Faça um programa que leia 2 notas de um aluno, calcule a média e imprima aprovado ou reprovado (para ser aprovado a média deve ser no mínimo 6).

nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segundanota do aluno: '))
nota = (nota1 + nota2) / 2
if nota >= 6:
    print ('Aluno aprovado!')
else:
    print('Aluno reprovado!')  