from banco import Banco

banco = Banco()

# Criar algumas contas iniciais só para testes
banco.criar_conta("Júlia", 200)
banco.criar_conta("Maria", 500)
banco.criar_conta("Lucas", 50)

print("\n=== LOGIN DO SISTEMA BANCÁRIO ===")

numero_digitado = int(input("Digite o número da sua conta: "))

conta = banco.buscar_conta(numero_digitado)

if conta:
    print(f"\nBem-vinda, {conta.nome}!")
    conta.mostrar_saldo()
else:
    print("\n❌ Conta não encontrada. Verifique o número e tente novamente.")
