# 11. Verificação de Diferente de Zero:
# Solicite ao usuário um número.
# Verifique se o número digitado é diferente de zero e exiba a mensagem correspondente.

while(1):
    numero = float(input("Digite um número: "))
    if numero != 0:
        print("O número digitado é diferente de zero!")
    else:
        print("O número é igual a zero!")
        break
