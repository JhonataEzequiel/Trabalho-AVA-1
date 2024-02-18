import matplotlib.pyplot as plt

# Dados
categorias = ['A', 'B', 'C', 'D', 'E']
valores = [7, 13, 5, 17, 10]

# Criando o gráfico de barras horizontais
plt.barh(categorias, valores, color='green')

# Adicionando título e rótulos dos eixos
plt.title('Gráfico de Barras Horizontais')
plt.xlabel('Valores')
plt.ylabel('Categorias')

# Mostrando o gráfico
plt.show()
