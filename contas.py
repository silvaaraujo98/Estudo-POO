class Conta:
    def __init__(self,clientes,número,saldo = 0):
        self.saldo = 0
        self.clientes = clientes
        self.número = número
        self.operacoes = []
        self.deposito(saldo)

    def resumo(self):
        for x in self.clientes:
            print(f"Cliente : {x.nome} Telefone : {x.telefone} CC Número : {self.número} Saldo : {self.saldo:10.2f}")

    def saque(self,valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(["SAQUE",valor])
        else:
            print(f"Você não tem saldo suficiente, seu saldo é R${self.saldo:5.2f}")

    def deposito(self,valor):
        self.saldo += valor
        self.operacoes.append(["DEPOSITO",valor])

    def extrato(self):
        print(f"Extrato CC N° {self.número}\n")
        for o in self.operacoes:
            print(f"{o[0]:10s} {o[1]:10.2f}")
        print(f"\n Saldo: {self.saldo:10.2f}\n")
class ContaEspecial(Conta):
    def __init__(self, clientes, número, saldo=0,limite=0):
        Conta.__init__(self,clientes,número,saldo)
        self.limite = limite

    def saque(self,valor):
        if self.saldo + self.limite >= valor:
            self.saldo-=valor
            self.operacoes.append(["SAQUE",valor])