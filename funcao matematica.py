import matplotlib.pyplot as plt
import numpy as np

# Dados
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Criando o gráfico da função seno
plt.plot(x, y, color='blue')

# Adicionando título e rótulos dos eixos
plt.title('Gráfico da Função Seno')
plt.xlabel('x')
plt.ylabel('sin(x)')

# Mostrando o gráfico
plt.grid(True)
plt.show()
