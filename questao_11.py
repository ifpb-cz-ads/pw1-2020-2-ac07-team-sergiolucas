# 11) Observe o método saque das classes Conta e ContaEspecial. Modifique o método
# saque da classe Conta de forma que a verificação da possibilidade de saque seja feita por
# um novo método, substituindo a condição atual. Esse novo método retornará verdadeiro se
# o saque puder ser efetuado, e falso em caso contrário. Modifique a classe ContaEspecial de
# forma a trabalhar com esse novo método. Verifique se você ainda precisa trocar o método
# saque de ContaEspecial ou apenas o novo método criado para verificar a possibilidade de
# saque


class Conta:
    def __init__(self, clientes, número, saldo = 0):
        self.saldo = 0
        self.clientes = clientes
        self.número = número
        self.operações = []
        self.deposito(saldo)

    def resumo(self):
        for cliente in self.clientes:
            print("Nome do CLiente: %s \nTefone: %s" % (cliente.nome, cliente.telefone))
        print("CC N°%s \nSaldo: %10.2f" %
              (self.número, self.saldo))

    def checar_saque(self, valor):
        return self.saldo >= valor

    def saque(self, valor):
        if self.checar_saque(valor):
            self.saldo -= valor
            self.operações.append(["SAQUE", valor])
            return True
        else:
            print("O Saldo da Conta comun é insuficiente !")
            return False

    def deposito(self, valor):
        self.saldo += valor
        self.operações.append(["DEPÓSITO", valor])

    def extrato(self):
        print("Extrato CC N° %s\n" % self.número)
        for o in self.operações:
            print("%10s %10.2f" % (o[0] ,o[1]))
        print("\n       Saldo: %10.2f\n" % self.saldo)


class ContaEspecial(Conta):
    def __init__(self, clientes, número, saldo = 0, limite=0):
        Conta.__init__(self, clientes, número, saldo)
        self.limite = limite

    def checar_saque(self, valor):
        if(self.saldo + self.limite >= valor):
            return True
        else:
            return False
