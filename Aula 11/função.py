
# Exemplo 1: Função que imprime o valor de uma variável global
x = 10

def imprimir_variavel():
    """Imprime o valor da variável global x"""
    print("Valor:", x)

imprimir_variavel()
print("-" * 40)

# Exemplo 2: Função que altera o valor de uma variável local
y = 5

def alterar_variavel():
    """Altera o valor da variável local y"""
    y = 10
    print("Alterou para:", y)

alterar_variavel()
print("-" * 40)

# Exemplo 3: Função que imprime a soma de dois valores fixos
def soma_fixa():
    """Soma dois valores fixos"""
    a = 2
    b = 3
    print("Soma fixa:", a + b)

soma_fixa()
print("-" * 40)

# Exemplo 4: Função com parâmetros
def soma(a, b):
    """Recebe dois valores e imprime sua soma"""
    print(f"Soma de {a} + {b} = {a + b}")

soma(10, 10)
print("-" * 40)

# Exemplo 5: Função com cálculo de diferença
def diferenca(c, d):
    """Exibe a diferença entre dois valores"""
    print("Diferença entre Max e Charles é:", c - d, "pontos")

diferenca(169, 138)
print("-" * 40)

# Exemplo 6: Função com parâmetro opcional
def saudacao(nome="Amigo"):
    """Exibe uma saudação personalizada"""
    print(f"Olá, {nome}!")

nome_digitado = input("Digite um nome: ")
saudacao(nome_digitado)
print("-" * 40)

# Exemplo 7: Função com múltiplos parâmetros opcionais
def multiplica(a, b=1):
    """Exibe dois valores, com o segundo sendo opcional"""
    print(f"Valores recebidos: a={a}, b={b}")

multiplica(4)
multiplica(4, 5)
print("-" * 40)

# Exemplo 8: Função com retorno de valor
def dobro(g):
    """Retorna o dobro do valor fornecido"""
    return g * 2

resultado = dobro(5)
print("Dobro de 5 é:", resultado)

