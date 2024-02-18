import matplotlib.pyplot as plt
import numpy as np

# Dados
dados = np.random.randn(1000)

# Criando o gráfico de histograma
plt.hist(dados, bins=30, cumulative=True, alpha=0.5, color='g')

# Adicionando título e rótulos dos eixos
plt.title('Histograma Acumulado')
plt.xlabel('Valores')
plt.ylabel('Frequência Acumulada')

# Mostrando o gráfico
plt.show()
