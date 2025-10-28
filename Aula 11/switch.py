def dias_da_semana(opção):
    match opção:
        case 1:
            return "Domingo"
        case 2:
            return "Segunda-feira"
        case 3:
            return "Terça-feira"
        case 4:
            return "Quarta-feira"
        case 5:
            return "Quinta-feira"
        case 6:
            return "Sexta-feira"
        case 7:
            return "Sábado"
        case _:
            return "Opção inválida"
        
#Solicitar ao usuário para inserir o numero
    
opção_usuario = int(input("Insira um numero de 1 a 7 para escolher o dia da semana:"))
    
#Chamar a função com a opção do usuário e imprimir o resultado
print(dias_da_semana(opção_usuario)) 
