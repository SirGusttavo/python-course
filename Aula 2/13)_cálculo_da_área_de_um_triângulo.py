# 13. Cálculo da Área de um Triângulo
# Crie um programa que calcule a área de um triângulo.

# Peça ao usuário para digitar a base e a altura do triângulo.
# Crie uma variável area para armazenar a área do triângulo, usando a fórmula area = (base * altura) / 2.
# Imprima o valor da área na tela.

base = float(input("Digite a base do triângulo:"))
altura = float(input("Digite a altura do triângulo:"))
area = (base*altura)/2
print ("A área do triângulo fornecido é de:","%.2f" % area)
