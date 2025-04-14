# 11. Cálculo de Valor com Juros
# Você está trabalhando em uma aplicação de vendas online e precisa de um programa que calcule o valor total de um produto, acrescentando 15% de juros sobre o preço original.

# Solicite ao usuário que insira o valor do produto.
# Calcule o valor dos juros usando a fórmula ValorJuros = ValorProduto * 0.15.
# Calcule o valor total com juros.
# Imprima o valor total com os 15% de juros no terminal.

ValorProduto = float(input("Digite o valor do produto:"))
ValorJuros = ValorProduto*0.15
ValorTotal = ValorProduto+ValorJuros
print ("O valor final do produto, com um pequeno juros de 15%:","%.2f" % ValorTotal)