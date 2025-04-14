# 12. Calculadora de Desconto: Escreva um programa que simule uma loja, onde o usuário insere o valor total de suas compras e o programa calcula o desconto a ser aplicado, de acordo com a seguinte tabela:
# Compras de até R$ 100,00: sem desconto
# Compras de R$ 100,01 a R$ 500,00: 5% de desconto
# Compras de R$ 500,01 a R$ 1000,00: 10% de desconto
# Compras acima de R$ 1000,00: 15% de desconto

compras = float(input("Digite o valor total das suas compras: "))
if compras <= 100.00:
    print ("Suas compras não atingiram o valor minímo de R$ 100,00, portanto o seu desconto é de:\n",compras * 0.00, "reais. \nO valor final de suas compras é de:", compras - (compras * 0.00)) 
elif compras >= 100.01 and compras <= 500.0:
    print ("Suas compras atingiram o valor minímo de R$ 100,00, portanto o seu desconto é de:\n", compras * 0.05, "reais. \nO valor final de suas compras é de:", compras - (compras * 0.05)) 
elif compras >= 500.01 and compras <= 1000.00:
    print ("Suas compras passaram de R$ 500,00, portanto o seu desconto é de:\n", compras * 0.10, "reais. \nO valor final de suas compras é de:", compras - (compras * 0.10))
else:
    print ("Suas compras pasasaram de R$ 1000,00, portanto o seu desconto é de:\n", compras * 0.15, "reais. \nO valor final de suas compras é de:", compras - (compras * 0.15))
