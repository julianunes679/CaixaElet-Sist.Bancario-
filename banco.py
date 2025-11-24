class Conta:
    contador_contas = 1000  # começa as contas em 1000

    def __init__(self, nome, saldo_inicial=0):
        self.numero = Conta.contador_contas
        Conta.contador_contas += 1  # gera próximo número

        self.nome = nome
        self.__saldo = saldo_inicial  # privado

    def depositar(self, valor):
        if valor <= 0:
            print("❌ Valor inválido para depósito.")
            return
        self.__saldo += valor
        print(f"💰 Depósito de R${valor} realizado.")

    def sacar(self, valor):
        if valor <= 0:
            print("❌ Valor inválido.")
            return
        if valor > self.__saldo:
            print("❌ Saldo insuficiente.")
            return
        self.__saldo -= valor
        print(f"🏧 Saque de R${valor} realizado.")

    def mostrar_saldo(self):
        print(f"📄 Conta {self.numero} | Dono: {self.nome} | Saldo: R${self.__saldo}")


class Banco:

    def __init__(self):
        self.contas = []  # lista de todas as contas

    def criar_conta(self, nome, saldo_inicial=0):
        nova = Conta(nome, saldo_inicial)
        self.contas.append(nova)
        print(f"✅ Conta criada com sucesso! Número: {nova.numero}")
        return nova

    def buscar_conta(self, numero):
        for conta in self.contas:
            if conta.numero == numero:
                return conta
        return None

