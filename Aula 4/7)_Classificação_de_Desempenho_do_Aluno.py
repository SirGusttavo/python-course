# 7. Classificação de Desempenho do Aluno:
# Solicite ao usuário a nota do aluno.
# Baseado na nota, classifique o aluno como excelente (nota >= 9), bom (nota >= 7), regular (nota >= 5) ou insatisfatório (nota < 5).

nota = float(input("Digite a nota do aluno: "))
if nota >= 9:
    print ("Aluno excelente!")
elif nota >= 7:
    print ("Aluno bom!")
elif nota >= 5:
    print ("Aluno regular!")
else:
    print ("Aluno insatisfatório!")