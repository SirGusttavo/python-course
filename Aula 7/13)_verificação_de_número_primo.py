# Pede ao usuário para digitar um número e converte para inteiro
numero = int(input("Digite um número: "))

# Números menores que 2 não são primos
if numero < 2:
    print("O número digitado NÃO é um número primo")
else:
    # Começamos assumindo que o número é primo
    eh_primo = True

    # Testamos se algum número de 2 até a raiz quadrada de 'numero' divide ele
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:  # Se dividir certinho, não é primo
            eh_primo = False
            break  # Não precisa testar mais, já achamos um divisor

    # Mostra o resultado com base no valor de 'eh_primo'
    if eh_primo:
        print("O número digitado é um número primo")
    else:
        print("O número digitado NÃO é um número primo")

if numero % 2
