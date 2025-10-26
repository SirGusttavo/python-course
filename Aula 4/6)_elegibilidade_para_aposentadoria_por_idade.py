# 6. Elegibilidade para Aposentadoria por Idade:
# Solicite ao usuário sua idade e sexo (masculino ou feminino).
# Se for do sexo feminino e tiver 60 anos ou mais, ou do sexo masculino e tiver 65 anos ou mais, exiba "Você pode solicitar a aposentadoria por idade.". Caso contrário, exiba "Você ainda não pode solicitar a aposentadoria por idade."

idade = int(input('Digite sua idade: '))
sexo = str(input('Qual o seu sexo: '))
lower = sexo.lower ()
if idade >= 60 and lower == 'feminino':
    print('Você pode se aposentar!')
elif idade >= 65 and lower == 'masculino':
    print('Você pode se aposentar!')
else:
    print('Você ainda não pode se aposentar!')
