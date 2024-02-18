import matplotlib.pyplot as plt
import numpy as np

# Dados
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Criando o gráfico
plt.plot(x, y1, '-g', label='seno(x)', linewidth=2) # Linha verde contínua
plt.plot(x, y2, ':r', label='cosseno(x)', linewidth=2) # Linha vermelha pontilhada

# Adicionando título e legenda
plt.title('Gráfico de Seno e Cosseno')
plt.legend(loc='upper right')

# Mostrando o gráfico
plt.grid(True)
plt.show()
