class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular        # público
        self.__saldo = saldo_inicial  # privado

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente ou valor inválido.")

    def ver_saldo(self):
        print(f"Saldo atual: R${self.__saldo:.2f}")

# ----- SISTEMA INTERATIVO -----

print("=== Bem-vindo ao Mini Caixa Eletrônico ===")

# Criando uma conta antes do menu
nome = input("Digite o nome do titular da conta: ")
conta = ContaBancaria(nome)

while True:
    print("\nEscolha uma opção:")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Ver saldo")
    print("4 - Sair")

    opcao = input("Digite o número da opção: ")

    if opcao == "1":
        valor = float(input("Valor do depósito: R$ "))
        conta.depositar(valor)

    elif opcao == "2":
        valor = float(input("Valor do saque: R$ "))
        conta.sacar(valor)

    elif opcao == "3":
        conta.ver_saldo()

    elif opcao == "4":
        print("Saindo... Obrigada por usar nosso sistema!")
        break

    else:
        print("Opção inválida, tente novamente.")
