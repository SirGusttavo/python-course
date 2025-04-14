print("====CONVRSÃO CELCIUS/FAHRENHEIT====")
conversao = (input("Para converter Celcius para Fahrenheit digite 1, caso não, digite 2: "))
if conversao == "1":
    c1 = int(input("Digite a temperatura em Graus Celcius: "))
    c2 = (c1 * 1.8) + 32
    print("A temperatura atual é de", "%.2f"%c2, "°F")
elif conversao == "2":
    f1 = int(input("Digite a temperatura em Fahrenheit: "))
    f2 = (f1 - 32) / 1.8
    print("A temperatura atual é de", "%.2f"%f2, "°C")
else:
    print("Operação inválida! Digite um indicador de temperatura válido")
