class ContaBancaria:
    def __init__(self, titular, saldo = 0):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor} realizado com sucesso na conta de {self.titular}.")
        
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso na conta de {self.titular}.")
        else:
            print("saldo insuficiente")
            
    def mostrar_saldo(self):
        print(f"saldo atual de {self.titular}: R${self.saldo}")
        
#Criação de contas

contas = {
    "Gustavo": ContaBancaria("Gustavo Rafael", 1000),
    "Yan Botelho": ContaBancaria("Yan Botelho", 1000)
}

#Interface de banco

def banco_interface():
    while True:
        titular = input("Digite o nome do cliente (Gustavo Rafael ou Yan Botelho) ou 'sair' para encerrar: ")
        if titular == "sair":
            break
        if titular in contas:
            action = input("Digite 'saldo' para verificar o saldo, 'depositar' para depositar ou 'sacar' para sacar: ")
            
            
            
            if action == "saldo":
                contas[titular].mostrar_saldo()
            elif action in ["depositar", "sacar"]:
                valor = float(input("Digite o valor: R$"))
                if action == "depositar":
                    contas[titular].depositar(valor)
                else:
                    contas[titular].sacar(valor)
            else:
                print("Ação inválida")
        else:
            print("Cliente não encontrado")
            
#Chamar a função interface do banco de dados

banco_interface()
                