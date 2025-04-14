compras = float(input("Digite o valor total das suas compras: "))
desconto = int(input("Digite a porcentagem do seu desconto: "))
valor = compras - (compras * (desconto/100))
print ("O valor final das suas compras é de", "%.2f" % valor, "reais")