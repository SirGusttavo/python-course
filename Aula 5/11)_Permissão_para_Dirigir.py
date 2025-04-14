# 11. Permissão para Dirigir: 
# Crie um programa que pergunte ao usuário sua idade e se possui carteira de motorista. Se tiver menos de 18 anos, informe que não pode dirigir. Se tiver 18 anos ou mais, informe se pode dirigir ou não, dependendo se possui carteira de motorista ou não.

idade = int(input('Digite sua idade: '))
carteira = str(input('Você possui carteira da motorista? Digite sim ou não: '))
lower = carteira.lower ()
if idade >= 18 and lower == 'sim':
    print('Você pode digirir!')
else:
    print('Você não pode digirir!')