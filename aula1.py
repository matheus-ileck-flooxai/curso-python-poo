# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (istâncias) que
# podem ter seus próprio atributos e mêtodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de Classes

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Matheus', 'Ileck')


print(p1.nome)