print ("====Calculadora de Juros Simples====")
cp = float(input("Digite a Capital Inicial: "))
tj = float(input("Digite os valor da Taxa de Juros: "))
tp = int(input("Digite o valor do Tempo em minutos: "))
valor = (tj/100)*cp
montante = (valor + cp) * tp
print ("A montante final é", "%.2f" % montante)