from banco import Banco

b = Banco()
b.criar_conta("Julia", 200)
b.criar_conta("Maria", 500)
b.criar_conta("Lucas", 50)

conta = b.buscar_conta(1001)
if conta:
    conta.mostrar_saldo()