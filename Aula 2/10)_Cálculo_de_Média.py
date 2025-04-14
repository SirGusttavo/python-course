# 10. Cálculo de Média
# Peça ao usuário para digitar as notas de três provas.
# Armazene as notas nas variáveis nota1, nota2 e nota3.
# Calcule a média das notas usando a fórmula media = (nota1 + nota2 + nota3) / 3.
# Armazene o resultado na variável media.
# Imprima o valor da variável media no terminal.

nota1 = float(input("Digite a nota da 1° prova:"))
nota2 = float(input("Digite a nota da 2° prova:"))
nota3 = float(input("Digite a nota da 3° prova:"))
media = (nota1 + nota2 + nota3)/3
print ("A média final das provas é:","%.1f" % media)