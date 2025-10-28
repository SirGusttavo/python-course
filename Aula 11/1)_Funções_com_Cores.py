# Faça uma função usando nomes de Cores, utilizando match, def e case:

def cores(opção):
    match opção:
        case 1:
            return "Azul"
        case 2:
            return "Vermelho"
        case 3:
            return "Amarelo"
        case 4:
            return "Verde"
        case 5:
            return "Preto"
        case 6:
            return "Laranja"
        case 7:
            return "Branco"
        case 8:
            return "Roxo"
        case 9:
            return "Rosa"
        case _:
            return "Opção Inválida"
opção_usuario = int(input("Insira um número de 1 a 9 para escolher uma cor:"))
print(cores(opção_usuario)) 