# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 2024

@author: Prof. Dr. Monteiro, E. S.

Prompt:
Para o dataset "Populacao_censos_v5.csv" escreva um programa em python que faça uma análise da tendência 
da população dos municípios ao longo dos anos. 
Gere o resultado na tela e na forma de gráficos. 
Os gráficos devem ser saltos em formato JPG na pasta "graficos_populacao"
O programa deverá gerar o resultado na saída padrão ou seja na tela, 
mostrando resultados em texto e gráficos. 
Cada gráfico deverá ser um arquivo JPG separados.
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

# Carregar o arquivo CSV com o separador correto
file_path = 'Populacao_censos_v5.csv'
df = pd.read_csv(file_path, sep=';')

# Renomear as colunas de forma adequada (se já não estiverem corretas)
df.columns = ['Estado', 'Mesorregiao', 'Microrregiao', 'Municipio', '1980', '1991', '2000', '2010', '2022']

# Converter as colunas de população para tipo numérico (inteiro)
for year in ['1980', '1991', '2000', '2010', '2022']:
    df[year] = pd.to_numeric(df[year], errors='coerce')

# Criar diretório para salvar os gráficos
output_dir = 'graficos_populacao'
os.makedirs(output_dir, exist_ok=True)

# Função para gerar gráficos de tendência populacional
def plot_population_trend(df, municipio):
    # Filtrar os dados para o município selecionado
    data = df[df['Municipio'] == municipio]
    
    # Verificar se há dados de população para o município
    if data.empty or data[['1980', '1991', '2000', '2010', '2022']].isnull().all().all():
        print(f"Dados indisponíveis para o município: {municipio}")
        return

    # Obter os anos e populações, ignorando valores nulos
    anos = ['1980', '1991', '2000', '2010', '2022']
    populacao = data[anos].values.flatten()

    # Mostrar os resultados numéricos na tela
    print(f"\nTendência populacional para {municipio}:")
    for ano, pop in zip(anos, populacao):
        print(f"{ano}: {pop} habitantes")

    # Criar o gráfico
    plt.figure(figsize=(8, 6))
    plt.plot(anos, populacao, marker='o', linestyle='-', color='b')
    plt.title(f'Tendência Populacional - {municipio}')
    plt.xlabel('Ano')
    plt.ylabel('População')
    plt.grid(True)
    
    # Salvar o gráfico em formato JPG antes de exibir
    output_path = os.path.join(output_dir, f'tendencia_{municipio}.jpg')
    plt.savefig(output_path)
    
    # Exibir o gráfico na tela
    plt.show()

    # Fechar a figura após salvar e exibir
    plt.close()

# Gerar gráficos para cada município
municipios = df['Municipio'].unique()
for municipio in municipios:
    plot_population_trend(df, municipio)

print("Gráficos gerados e salvos na pasta:", output_dir)
