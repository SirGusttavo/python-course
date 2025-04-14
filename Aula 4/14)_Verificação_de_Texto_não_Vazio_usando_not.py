# 14. Verificação de Texto não Vazio usando not:
# Solicite ao usuário que digite algo.
# Verifique se o texto digitado não está vazio usando o operador not e exiba a mensagem correspondente.

texto = str(input("Digite algo: "))
if not texto == "":
        print("A caixa de texto está vazia")
else:
    print("A caixa de texto não está vazia")   