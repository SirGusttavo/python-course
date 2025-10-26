# 4. Intervalo Numérico:
# Solicite ao usuário um número.
# Verifique se o número está entre 10 e 20 (inclusive) e exiba a mensagem correspondente.

numero = float(input("Digite um número: "))
if numero >= 10 and numero <=20:
    print('Seu número está entre 10 e 20!')
else:
    print('Seu número está fora dos limites, por favor digite um número entre 10 e 20')
