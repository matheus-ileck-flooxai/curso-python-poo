# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

import json

CAMINHO_ARQUIVO = 'aula6.json'

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa('Matheus', 'Ileck')
p2 = Pessoa('Larissa', 'Ileck')
p3 = Pessoa('Zedao', 'Ileck')

bd = [vars(p1), vars(p2), vars(p3)]


def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w') as arquivo:
        print('Fazendo Dump:')
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)