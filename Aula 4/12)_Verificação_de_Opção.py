# 12. Verificação de Opção:
# Solicite ao usuário que selecione uma opção ("Sair" ou "Continuar").
# Verifique se a opção selecionada é diferente de "Sair" e exiba a mensagem correspondente.

opcao = str(input("Deseja sair ou continuar? "))
if opcao.lower() == "continuar":
    print("Você escolheu continuar!")
elif opcao.lower() == "sair":
    print("Você escolheu sair!")
else:
    print("Opção inválida!") 