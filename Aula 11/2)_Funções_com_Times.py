#Faça uma função usando nomes de Times, utilizando match, def e case:

def times(opção):
    match opção:
        case 1:
            return "São Paulo"
        case 2:
            return "Bota Fogo"
        case 3:
            return "Vasco"
        case 4:
            return "Fluminense"
        case 5:
            return "Flamengo"
        case 6:
            return "Palmeiras"
        case 7:
            return "Corinthians"
        case 8:
            return "Atlético"
        case 9:
            return "Cruzeiro"
        case _:
            return "Opção Inválida"
opção_usuario = int(input("Insira um número de 1 a 9 para escolher um time:"))
print(times(opção_usuario)) 