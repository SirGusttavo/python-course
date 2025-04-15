# 1. Cadastro de Pessoas:
# Você deve criar um programa em Python que faça o cadastro dos dados de um usuário. O programa deve solicitar as seguintes informações:

# Nome
# Sobrenome
# Idade
# Data de nascimento
# Telefone
# Endereço (rua)
# Número de residência
# Bairro
# Cidade
# Estado
# País
# Após coletar todas as informações, o programa deve imprimir na tela todos os dados cadastrados de forma organizada.
nome = input ('Seu nome:')
sobrenome = input ('Seu sobrenome:')
idade = input ('Sua idade:')
nascimento = input ('Sua data de nascimento:')
telefone = input ('Seu telefone:')
endereço = input ('Seu endereço:')
número = input ('Seu número de residência:')
bairro = input ('Seu bairro:')
cidade = input ('Sua cidade:')
estado = input ('Seu estado:')
país = input ('Seu país:')
print('=====Cadastro=====')
print('\nSeu nome :', nome,sobrenome,'\nVocê tem:', idade,'\nVocê nasceu em:', nascimento,'\nSeu número de telefone é:', telefone,'\nSeu endereço completo é:', endereço, número, bairro, cidade, '\nSeu estado e país é:', estado, país)
print('Seu cadastro foi concluído, tenha um bom dia!')

