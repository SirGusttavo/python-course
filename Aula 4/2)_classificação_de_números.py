# 2. Classificação de Números:
# Solicite ao usuário que digite um número.
# Verifique se o número é positivo, negativo ou zero e imprima a respectiva mensagem.

numero =  int(input('Digite um número: '))
if numero > 0:
    print('O número digitado é positivo')
elif numero < 0:
    print('O número digitado é negativo')
else:
    print ('O número digitado é igual a zero')
    
