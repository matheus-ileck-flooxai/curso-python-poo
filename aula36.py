# namedtuples - tuplas imutáveis com nomes para valores
# Usamos namedtuples parar criar classes de objetos que são apenas um 
# agrupamento de atributos, como classes normais sem métodos, ou registros de 
# bases de dados, etc.
# as namedtuples são imutáveis assim como as tuplas

from collections import namedtuple

Carta = namedtuple('Carta', ['valor', 'naipe'])
as_espadas = Carta('A', '♠️')

print(as_espadas)
print(as_espadas[0])
print(as_espadas[1])
print(as_espadas.naipe)
print(as_espadas.valor)
