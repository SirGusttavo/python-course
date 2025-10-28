# ContaBancaria seria a classe na orientação do objeto
# Self seria a instancia para consumir e armazenar os valores
# def seria as funções para serem feitas
# += seria para pegar o valor atual com o valor inserido

class ContaBancaria:
    def __init__(self, titular, saldo__inicial):
        self.titular = titular
        self.saldo = saldo__inicial
        print(f"Saldo inicial: {self.saldo}")
        
    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de {valor} realizado. Saldo atual: {self.saldo}")
conta = ContaBancaria("Anna", 1000)
valor_depósito = float(input("Diigte o valor a ser depositado:"))
conta.depositar(valor_depósito)

print(f"SaLDO Final: {conta.saldo}") 