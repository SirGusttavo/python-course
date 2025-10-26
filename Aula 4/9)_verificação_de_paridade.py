# 9. Verificação de Paridade:
# Solicite ao usuário um número.
# Verifique se o número é par ou ímpar e exiba a mensagem correspondente.

numero = int(input("Digite um número: "))
par = numero % 2
if par == 0:
    print("O número digitado é um número par!")
else:
    print("O número digitado é um número ímpar!") 
