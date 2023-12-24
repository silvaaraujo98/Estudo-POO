class Banco:
    #Como atributo do Banco temos seu nome e a lista de contas
    #Como métodos temos a abertura de uma conta corrente e listagem de todas as contas do banco.
    def __init__(self,nome):
        self.nome = nome
        self.clientes = []
        self.contas =[]
    def abre_conta(self,conta):
        self.contas.append(conta)
    
    def lista_contas(self):
        for c in self.contas:
            c.resumo()

    
