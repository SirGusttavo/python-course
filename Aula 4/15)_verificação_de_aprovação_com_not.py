# 15. Verificação de Aprovação com not:
# Solicite ao usuário a nota do aluno.
# Verifique se a nota do aluno não é menor que 6 usando o operador not e exiba a mensagem correspondente.

nota = float(input("Digite a nota do aluno: "))
if not nota >= 6:
        print("Aluno aprovado!")
else:
    print("Aluno reprovado!")
    
