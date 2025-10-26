# 1. Permissão para Dirigir:
# Solicite ao usuário sua idade e se ele possui carteira de motorista.
# Se a idade for maior ou igual a 18 e ele possuir carteira de motorista, exiba "Você pode dirigir.". Caso contrário, exiba "Você não pode dirigir."


idade = int(input('Digite sua idade: '))
carteira = str(input('Você possui carteira da motorista? Digite sim ou não: '))
lower = carteira.lower ()
if idade >= 18 and lower == 'sim':
    print('Você pode digirir!')
else:
    print('Você não pode digirir!')
