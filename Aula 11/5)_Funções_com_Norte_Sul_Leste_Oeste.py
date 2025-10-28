#Faça uma função usando direções, como Norte, Sul, Leste e Oeste, utilizando match, def e case:

def direções(opção):
    match opção:
        case 1:
            return "Norte"
        case 2:
            return "Sul"
        case 3:
            return "Leste"
        case 4:
            return "Oeste"
        case 5:
            return "Nordeste"
        case 6:
            return "Sudeste"
        case 7:
            return "Noroeste"
        case 8:
            return "Sudoeste"
        case _:
            return "Opção Inválida"
opção_usuario = int(input("Insira um número de 1 a 9 para escolher uma direção:"))
print(direções(opção_usuario)) 