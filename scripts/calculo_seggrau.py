"""
resolve funcoes do segundo grau
emitir valores de y, lista
+ coeficientes
lista[y] = a * lista[x] ** 2 + b * lista[x] + c
"""


class EquancaoQuadratica:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.listay = []
        self.listax = list(range(-1, 10))

    def get_resultado(self):
        for pontos_x in self.listax:
            resultado = self.a * (self.listax[pontos_x] ** 2) + self.b * self.listax[pontos_x] + self.c
            self.listay.insert(pontos_x, resultado)
        return self.listay


if __name__ == '__main__':
    qd = EquancaoQuadratica(1, -6, 8)
    qd.get_resultado()
    print(qd.listax)
    print(qd.listay)
