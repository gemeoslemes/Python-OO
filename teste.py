from conta import Conta
# Criando conta
conta = Conta(123, "Victor", 100.0, 1000.0)
# Criando a segunda conta
conta2 = Conta(321, "Vinicius", 50.0, 1000.0)
# Criando a terceira conta
conta3 = Conta(444, "João Batista", 200.0, 1000)
#Transferindo da conta para a segunda conta passando primeiro o valor
conta.transfere(10, conta2)

conta.extrato()
conta2.extrato()

#Testando metodos estaticos
print("Banco do Brasil: {}".format(Conta.codigo_banco()))
print("Bancos: {}".format(Conta.codigos_bancos()))
#
print("Nome do titular: {}".format(conta.titular))
print("Saldo da Conta: {}".format(conta.saldo))
print("Limite da conta: {}".format(conta.limite))

conta3.saca(2000)
