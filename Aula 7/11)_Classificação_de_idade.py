print('====Classificação de idade====')
idade = int(input('Digite sua idade: '))
if idade >=0 and idade <=12:
    print('Você está classificado como Criança!')
elif idade >=13 and idade <=17:
    print('Você está classificado como Adolescente!')
elif idade >=18 and idade <=64:
    print('Você está classificado como Adulto (a)!')
else:
    print('Você está classificado como Idoso (a)!') 