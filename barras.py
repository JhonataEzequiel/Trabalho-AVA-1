import matplotlib.pyplot as plt

# Dados
categorias = ['A', 'B', 'C', 'D', 'E']
valores = [7, 13, 5, 17, 10]
cores = ['blue', 'orange', 'green', 'red', 'purple']

# Criando o gráfico de barras
plt.bar(categorias, valores, color=cores)

# Adicionando título e rótulos dos eixos
plt.title('Gráfico de Barras')
plt.xlabel('Categorias')
plt.ylabel('Valores')

# Mostrando o gráfico
plt.show()
