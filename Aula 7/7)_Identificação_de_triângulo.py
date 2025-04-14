medida1 = float(input("Digite a medida do primeiro lado do triângulo: "))
medida2 = float(input("Digite a medida do segundo lado do triângulo: "))
medida3 = float(input("Digite a medida do terceirp lado do triângulo: "))
if medida1 == medida2 == medida3:
    print("As medidas dos lados formam um triângulo equilátero!")
elif medida1 == medida2 != medida3 or medida1 == medida3 != medida2 or medida3 == medida2 != medida1:
    print("As medidas dos lados formam um triângulo isósceles!")
else:
    print("As medidas dos lados formam um triângulo escaleno!")