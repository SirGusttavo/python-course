# 6. Dia da Semana: 
# Faça um programa que peça ao usuário um número de 1 a 7 e mostre o dia da semana correspondente (1 para domingo, 2 para segunda-feira, etc.).

while(1):
    numero = int(input("Digite um número de 1 a 7: "))
    if numero <1 or numero >7:
        print("Número inválido!")
    elif numero == 1:
        print ("O número digitado corresponde ao dia da semana: Domingo")
    elif numero == 2:
        print ("O número digitado corresponde ao dia da semana: Segunda-feira")
    elif numero == 3:
        print ("O número digitado corresponde ao dia da semana: Terça-feira")   
    elif numero == 4:
        print ("O número digitado corresponde ao dia da semana: Quarta-feira")
    elif numero == 5:
        print ("O número digitado corresponde ao dia da semana: Quinta-feira")
    elif numero == 6:
        print ("O número digitado corresponde ao dia da semana: Sexta-feira")
    else:
        print ("O número digitado corresponde ao dia da semana: Sábado") 