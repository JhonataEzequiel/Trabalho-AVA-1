import matplotlib.pyplot as plt

# Dados
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho']
vendas = [100, 120, 90, 150, 200, 180]

# Criando o gráfico de área
plt.fill_between(meses, vendas, color="skyblue", alpha=0.4)
plt.plot(meses, vendas, color="Slateblue", alpha=0.6, linewidth=2)

# Adicionando título e rótulos dos eixos
plt.title('Vendas ao Longo do Tempo')
plt.xlabel('Meses')
plt.ylabel('Vendas')

# Mostrando o gráfico
plt.show()
