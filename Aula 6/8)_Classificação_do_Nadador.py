# 8. Classificação do Nadador: 
# Elabore um algoritmo que dada a idade de um nadador classifique-o em uma das seguintes categorias: Infantil A = 5 a 7 anos, Infantil B = 8 a 11 anos, Juvenil A = 12 a 13 anos, Juvenil B = 14 a 17 anos, Adultos = Maiores de 18 anos.



print('====Classificação de nadadores por idade====')
idade = int(input('Digite sua idade: '))
if idade >=5 and idade <=7:
    print('Você está classificado na categoria Infantil A!')
elif idade >=8 and idade <=11:
    print('Você está classificado na categoria Infantil B!')
elif idade >=12 and idade <=13:
    print('Você está classificado na categoria Juvenil A!')
elif idade >=14 and idade <=17:
    print('Você está classificado na categoria Juvenil B!')
else:
    print('Você está classificado na categoria Adulto!') 