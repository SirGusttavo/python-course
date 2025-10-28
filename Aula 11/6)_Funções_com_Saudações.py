#Faça uma função usando saudações, como Olá, Adeus, Bom dia e Boa noite, utilizando match, def e case:

def saudações(opção):
    match opção:
        case 1:
            return "Olá"
        case 2:
            return "Oi"
        case 3:
            return "Bom dia"
        case 4:
            return "Boa tarde"
        case 5:
            return "Boa noite"
        case 6:
            return "Adeus"
        case 7:
            return "Tchau"
        case 8:
            return "Até logo"
        case _:
            return "Opção Inválida"
opção_usuario = int(input("Insira um número de 1 a 9 para escolher uma saudação:"))
print(saudações(opção_usuario))   