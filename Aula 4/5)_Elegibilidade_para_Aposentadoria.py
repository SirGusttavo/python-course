# 5. Elegibilidade para Aposentadoria:
# Solicite ao usuário sua idade e o tempo de contribuição em anos.
# Se a idade for maior ou igual a 65 ou o tempo de contribuição for maior ou igual a 30 anos, exiba "Você pode se aposentar.". Caso contrário, exiba "Você ainda não pode se aposentar."

idade = int(input('Digite sua idade: '))
tempo = int(input('Digite seu tempo de contribuição em anos: '))
if idade >= 65 or tempo >= 30:
    print("Você pode se aposentar!")
else:
    print("Você ainda não pode se aposentar!")