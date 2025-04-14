#for elemento in range (1,10,2):
  #  print(elemento)
#print("Fim")

'''inicio = int (input("Informe o primeiro número: "))
fim = int(input("Informe o número final: "))
salto = int(input("Informe o salto: "))
texto = "Cálculo: "
soma  = 0
for numero in range (inicio,fim,salto):
    soma = soma + numero
    texto = texto + str(numero)
    if numero > 50:
    texto = texto + "\nPassou de 50"
    break
if numero != fim -1:
    texto = texto + "+"
print (f"{texto}")
print (f"Soma: {soma}")
'''

'''print("Fatorial de 5 (5!):")
numero = 1
for elemento in range (1,6):
    numero = elemento * numero
    print (numero)
print (f"5! = {numero}")
'''

'''for caracter in "Senai":
    print(caracter)'''
''    
'''listanome = ["Sillas","Guga","Born"]
for elemento in listanome:
    print (elemento)
    if elemento == "Guga":
        break
    '''
'''for x in [1, 10, 20, 30, 40, 50]:
    if x == 30:
        continue
    print(x)'''
'''    
for mult in range (1,500,2):
    if mult % 3==0:
        print(mult)'''
        
'''num = 3
for numero in range (3,500,6):
    num = numero*num

    '''
    
'''print("====TABUADA SIMPLES====")
numero1 = int(input("Digite um número que deseja saber a tabuada: ")) 
final = int(input("Digite o número multiplicador final da tabuada: ")) 
for mult in range (0,final):
    if mult % numero1 == 0:
        print(mult)
        '''
'''x = 1
while x<100000000000:
    print(x)
    x = x + 1'''
    
while True:
    resposta = str(input("Deseja sair do programa: (Sim ou Não)"))
    if resposta.lower() == "sim":
        print("Saindo...")
        break
    print("Você escolheu ficar!")
    continue