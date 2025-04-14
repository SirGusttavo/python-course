# 9. Operações Matemáticas: 
# Faça um programa que solicite dois números ao usuário (com decimais) Em seguida solicite que o usuário informe o resultado das quatro operações matemáticas ( subtração, multiplicação e divisão).

numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))
som = numero1 + numero2
sub = numero1 - numero2 
mult = numero1 * numero2
div = numero1 / numero2
soma = float(input('Digite o resultado da soma dos dois números (limitado a duas casas decimais):'))
subtracao = float(input('Digite o resultado da subtração dos dois números (limitado a duas casas decimais):'))
multiplacacao = float(input('Digite o resultado da multiplcação dos dois números (limitado a duas casas decimais):'))
divisao = float(input('Digite o resultado da divisão dos dois números (limitado a duas casas decimais):'))
if som == soma and sub == subtracao and mult == multiplacacao and div == divisao:
    print ('Parábens você acertou!')
else:
    print('Seu burro, você errou! O resultado era:',
        '%.2f'% som,
          '%.2f' % sub,
          '%.2f' % mult,
          '%.2f'% div)




