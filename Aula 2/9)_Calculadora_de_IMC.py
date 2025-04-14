# 9. Calculadora de IMC
# Peça ao usuário para digitar sua altura e peso.
# Armazene os valores nas variáveis altura e peso.
# Calcule o IMC usando a fórmula imc = peso / (altura * altura).
# Armazene o resultado na variável imc.
# Imprima o valor da variável imc no terminal.

peso = float(input("Digite seu peso:"))
altura = float(input("Digite sua altura:"))
imc = peso / (altura*altura)
print ("O seu IMC é:","%.2f" % imc)