# 8. Simulador de Calculadora: 
# Faça um programa que simule uma calculadora simples, onde o usuário insere dois números e escolhe a operação matemática (soma, subtração, multiplicação ou divisão).

print("===Calculadora Simples===")
while(1):
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    operacao = str(input("'Digite a operação:\n +\n -\n *\n /\n"))
    if operacao == "+":
        print("O valor da soma é:", numero1 + numero2)
    elif operacao == "-":
        print("O valor da subtração é:", numero1 - numero2)
    elif operacao == "*":
        print("O valor da multiplicação é:", numero1 * numero2)
    else:
        print("O valor da divisão é:", numero1 / numero2)
    
    