#Faça uma função usando nomes de Animais, utilizando match, def e case.Faça com nome de animais:

def animais(opção):
    match opção:
        case 1:
            return "Cachorro"
        case 2:
            return "Gato"
        case 3:
            return "Vaca"
        case 4:
            return "Boi"
        case 5:
            return "Lobo"
        case 6:
            return "Passáro"
        case 7:
            return "Hamster"
        case 8:
            return "Rato"
        case 9:
            return "Galo"
        case _:
            return "Opção Inválida"
opção_usuario = int(input("Insira um número de 1 a 9 para escolher um animal:"))
print(animais(opção_usuario)) 