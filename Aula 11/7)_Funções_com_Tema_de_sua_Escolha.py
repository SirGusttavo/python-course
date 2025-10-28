#Faça com tema de sua escolha:

def jogos(opção):
    match opção:
        case 1:
            return "God of War"
        case 2:
            return "Uncharted"
        case 3:
            return "The Last of Us"
        case 4:
            return "Spider Man"
        case 5:
            return "Batman Arkhan Knight"
        case 6:
            return "Crash Bandicoot"
        case 7:
            return "Sonic"
        case 8:
            return "Super Mario World"
        case 9:
            return "Resident Evil"
        case _:
            return "Opção Inválida"
opção_usuario = int(input("Insira um número de 1 a 9 para escolher um jogo:"))
print(jogos(opção_usuario)) 