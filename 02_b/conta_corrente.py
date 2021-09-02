class ContaCorrente:

    def __init__(self, limite, saldo):
        self.limite = 100
        self.saldo = 0

    def get_limite(self):
        print("Seu limite atual é de 100")
        print("saldo atual é de: ", self.saldo)

    saldo = 0
    while saldo  != 100:
        print("você ainda possui limite disponivel")
