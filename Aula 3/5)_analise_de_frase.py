# 5. Análise de Frase
# Faça um programa que leia uma frase pelo teclado e mostre:

# Quantas vezes aparece a letra "A".
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a última vez.

frase = str(input('Digite sua frase: '))
a = frase.count('a')
A = frase.count('A')
â = frase.count('â')
Â = frase.count('Â')
á = frase.count('á')
Á = frase.count('Á')
à = frase.count('à')
À = frase.count('À')
ã = frase.count('ã')
soma = a + A + â + Â + á + Á + à + À + ã
print ('A letra "a" aparece', soma,'vezes')
soma = frase.find('a')
print ('A primeira vez que letra "a" aparece, está na posição',soma)
soma = frase.rfind('a')
print ('A última vez que letra "a" aparece, está na posição',soma)
