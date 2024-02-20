import json
import pandas as pd
import matplotlib.pyplot as plt

dados = None
with open("info.json") as f:
    dados = json.load(f)

pb_stats = dados["PB"]["stats"]
rj_stats = dados["RJ"]["stats"]

medias_pb = [pb_stats["media_notas_ch"], pb_stats["media_notas_lc"], pb_stats["media_notas_cn"], pb_stats["media_notas_mt"]]
medias_rj = [rj_stats["media_notas_ch"], rj_stats["media_notas_lc"], rj_stats["media_notas_cn"], rj_stats["media_notas_mt"]]

col = ['medias_ch', 'medias_lc', 'medias_cn', 'medias_mt']
plt.figure(figsize=(10, 5))
bars_pb = plt.bar(col, medias_pb, color='blue', label='Paraíba', alpha=0.7, width=-0.4, align='edge')
bars_rj = plt.bar(col, medias_rj, color='red', label='Rio de Janeiro', alpha=0.7, width=0.4, align='edge')

plt.bar_label(bars_pb, padding=1, fmt='%.2f')
plt.bar_label(bars_rj, padding=1, fmt='%.2f')

plt.title('Médias das notas do Enem 2022')

categories = ['Ciências Humanas', 'Linguagens e Códigos', 'Ciências da Natureza', 'Matemática']
plt.xticks(ticks=range(len(categories)), labels=categories, rotation=0)
plt.ylim(0, 650)
plt.yticks([])

plt.legend(loc='upper center')
plt.tight_layout()
plt.show()