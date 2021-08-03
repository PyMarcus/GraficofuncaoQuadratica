from calculo_seggrau import EquancaoQuadratica
import matplotlib.pyplot as plt


eq = EquancaoQuadratica(2, -6, 8)
eq.get_resultado()
x = eq.listax
y = eq.listay
plt.plot(x, y, c='red', linewidth=3)
plt.title('Função quadrática')
plt.show()
