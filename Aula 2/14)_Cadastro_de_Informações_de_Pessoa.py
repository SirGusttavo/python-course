# 14. Cadastro de Informações de Pessoa
# Crie um programa em Python chamado cadastro_pessoas.py. No programa, crie variáveis para armazenar informações sobre uma pessoa, incluindo pelo menos os seguintes itens:

# Nome
# Sobrenome
# Idade
# E-mail
# Endereço
# Cidade
# Estado
# Profissão
# Número de telefone
# Estado civil
# Nacionalidade
# Escolaridade
# Após coletar todas as informações, imprima-as na tela de forma organizada.

nome = input ('Seu nome:')
sobrenome = input ('Seu sobrenome:')
idade = input ('Sua idade:')
email = input ('Seu email:')
endereço = input ('Seu endereço:')
cidade = input ('Sua cidade:')
estado = input ('Seu estado:')
profissao = input ('Sua profissão:')
numerodetelefone = input ('Seu telefone:')
estadocivil = input ('Seu estado civil:')
nacionalidade = input ('Sua nacionalidade:')
escolaridade = input ('Seu nível de escolaridade:')
print('=====Cadastro=====')
print('\nSeu nome é:', nome,sobrenome,'\nVocê tem:', idade,'anos de idade','\nSeu endereço de email é:',email,'\nSeu endereço é:',endereço,'\nVocê vive em:',cidade,estado,'\nSua profissão é:',profissao,
      '\nSeu número de telefone é:',numerodetelefone,'\nSeu atual estado civil é:',estadocivil,'\nDe acordo com a sua nacionalidade você é:',nacionalidade,'\nSeu nível de escolaridade é:',escolaridade)
print('Seu cadastro foi concluído, tenha um bom dia!')