import pessoas
import contas

class Cliente(pessoas.Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.conta: contas.Conta | None = None # Opcional

