# 13. Verificação de Número Diferente de Zero usando not:
# Solicite ao usuário um número.
# Verifique se o número digitado é diferente de zero usando o operador not e exiba a mensagem correspondente.

numero = float(input("Digite um número: "))
if not numero != 0:
        print("O número digitado é diferente de zero!")
else:
    print("O número é igual a zero!")
