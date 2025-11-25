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

    # ---- MENU DENTRO DA CONTA ----
    def menu_conta(conta):
        while True:
            print("\n=== MENU DA CONTA ===")
            print("1 - Ver saldo")
            print("2 - Depositar")
            print("3 - Sacar")
            print("4 - Sair da conta")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                print(f"💰 Saldo atual: R${conta.get_saldo()}")

            elif opcao == "2":
                valor = float(input("Valor para depósito: R$"))
                conta.depositar(valor)

            elif opcao == "3":
                valor = float(input("Valor para saque: R$"))
                conta.sacar(valor)

            elif opcao == "4":
                print("Saindo da conta...")
                break

            else:
                print("❌ Opção inválida! Tente novamente.")

    # Chama o menu da conta
    menu_conta(conta)

else:
    print("\n❌ Conta não encontrada. Verifique o número e tente novamente.")
