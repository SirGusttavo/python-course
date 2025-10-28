# Exemplo 1: Contagem com range() e salto personalizado
for elemento in range(1, 10, 2):
    print(elemento)
print("Fim\n")

# Exemplo 2: Somatório com limite e salto definidos pelo usuário
inicio = int(input("Informe o primeiro número: "))
fim = int(input("Informe o número final: "))
salto = int(input("Informe o salto: "))

texto = "Cálculo: "
soma = 0

for numero in range(inicio, fim, salto):
    soma += numero
    texto += str(numero)
    if numero > 50:
        texto += "\nPassou de 50"
        break
    if numero != fim - 1:
        texto += " + "

print(f"{texto}")
print(f"Soma: {soma}\n")

# Exemplo 3: Cálculo de fatorial simples
print("Fatorial de 5 (5!):")
resultado = 1
for elemento in range(1, 6):
    resultado *= elemento
    print(resultado)
print(f"5! = {resultado}\n")

# Exemplo 4: Iteração sobre uma string
for caracter in "Senai":
    print(caracter)
print()

# Exemplo 5: Iteração sobre uma lista e uso do break
nomes = ["Sillas", "Gustavo", "Gabriel"]
for nome in nomes:
    print(nome)
    if nome == "Gustavo":
        break
print()

# Exemplo 6: Uso do continue para pular valores específicos
for x in [1, 10, 20, 30, 40, 50]:
    if x == 30:
        continue
    print(x)
print()

# Exemplo 7: Exibir números ímpares múltiplos de 3
for mult in range(1, 50, 2):
    if mult % 3 == 0:
        print(mult)
print()

# Exemplo 8: Estrutura while com condição de parada
while True:
    resposta = input("Deseja sair do programa? (Sim ou Não): ").strip().lower()
    if resposta == "sim":
        print("Saindo...")
        break
    print("Você escolheu ficar!\n")
