# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Carregar o dataset com o delimitador correto
df = pd.read_csv('Populacao_censos_v5.csv', delimiter=';')

# Filtrar para o ano de 2022
df_2022 = df[['Municipios', '2022']].copy()

# Renomear a coluna '2022' para algo mais descritivo
df_2022.columns = ['Municipios', 'Populacao_2022']

# Remover valores nulos (caso existam)
df_2022.dropna(subset=['Populacao_2022'], inplace=True)

# Ordenar os municípios pela população
df_2022 = df_2022.sort_values('Populacao_2022', ascending=False)

# Criar o Tree Map
plt.figure(figsize=(12, 8))
squarify.plot(sizes=df_2022['Populacao_2022'], label=df_2022['Municipios'], alpha=0.8)
plt.axis('off')  # Esconder os eixos
plt.title('Tree Map da População por Município em 2022')

# Salvar o gráfico como JPG
plt.savefig('treemap_populacao_municipios.jpg', format='jpg', dpi=300, bbox_inches='tight')

# Mostrar o gráfico na tela
plt.show()

