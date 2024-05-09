class Cliente:
    def __init__(self, nome, fone):
        self.nome = nome
        self.telefone = fone

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome