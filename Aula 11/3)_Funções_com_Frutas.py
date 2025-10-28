#Faça uma função usando nomes de Frutas, utilizando match, def e case:

def frutas(opção):
    match opção:
        case 1:
            return "Maçã"
        case 2:
            return "Banana"
        case 3:
            return "Manga"
        case 4:
            return "Uva"
        case 5:
            return "Pera"
        case 6:
            return "Mamão"
        case 7:
            return "Melão"
        case 8:
            return "Kiwi"
        case 9:
            return "Jabutica"
        case _:
            return "Opção Inválida"
opção_usuario = int(input("Insira um número de 1 a 9 para escolher um fruta:"))
print(frutas(opção_usuario)) 