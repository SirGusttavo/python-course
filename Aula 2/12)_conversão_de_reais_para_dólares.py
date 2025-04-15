# 12. Conversão de Reais para Dólares
# Você está comprando um produto importado e gostaria de saber o valor em reais que irá pagar após a conversão para dólares americanos.

# Peça ao usuário para digitar o valor em reais.
# Peça ao usuário para digitar a cotação atual do dólar.
# Calcule o valor em dólares usando a fórmula: valorDolar = valorReal / cotacaoDolar.
# Exiba o valor em reais, a cotação do dólar e o valor em dólares na tela.

valorReal = float(input("Digite o valor do produto:"))
cotacaoDolar = float(input("Digite a cotação atual do dólar:"))
valorDolar = valorReal / cotacaoDolar
print ("\nO valor do produto em Reais é",valorReal,"\n No entanto com a cotação atual do Dólar $",cotacaoDolar,",o produto fica:$","%.2f" % valorDolar)
