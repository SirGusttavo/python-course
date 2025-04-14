# 9. Aposentadoria: 
# Crie um programa que solicite ao usuário o seu gênero e idade e, com base nesses dados, decida se ele deve se aposentar ou não (homens com 65 anos ou mais e mulheres com 60 anos ou mais podem se aposentar).

idade = int(input('Digite sua idade: '))
sexo = str(input('Qual o seu sexo: '))
lower = sexo.lower ()
if idade >= 60 and lower == 'feminino':
    print('Você pode se aposentar!')
elif idade >= 65 and lower == 'masculino':
    print('Você pode se aposentar!')
else:
    print('Você ainda não pode se aposentar!')