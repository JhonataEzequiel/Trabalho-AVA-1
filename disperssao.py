import matplotlib.pyplot as plt
import numpy as np

# Dados
x = np.random.rand(50)
y = np.random.rand(50)
cores = np.random.rand(50)
tamanhos = 1000 * np.random.rand(50)

# Criando o gráfico de dispersão
plt.scatter(x, y, s=tamanhos, c=cores, alpha=0.5)

# Adicionando título e rótulos dos eixos
plt.title('Gráfico de Dispersão')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Mostrando o gráfico
plt.show()
