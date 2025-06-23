# Classes decoradoras (Decorator classes)

class Multiplicar:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        resultado = self.func(*args, **kwargs)
        return resultado
@Multiplicar
def soma(x,y):
    return x + y

dois_mais_dois = soma(2,2)
print(dois_mais_dois)