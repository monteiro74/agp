# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 2024

@author: Prof. Dr. Monteiro, E. S.

Prompt:
Gere um programa em python que use o dataset "Populacao_censos_v5.csv"
Faça uma análise do declínio populacional, indicando: municípios que tiveram diminuição da população ao longo do tempo. 
Mostre os resultados na saída padrão (tela) com textos e gráficos.
Grave os gráficos gerados em arquivos JPG
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

# Carregar o arquivo CSV
file_path = 'Populacao_censos_v5.csv'
df = pd.read_csv(file_path)

# Separar os dados em colunas utilizando o delimitador ';'
df_cleaned = df['Estado;Mesorregiao;Microrregiao;Municipios;1980;1991;2000;2010;2022'].str.split(';', expand=True)

# Renomear as colunas de forma adequada
df_cleaned.columns = ['Estado', 'Mesorregiao', 'Microrregiao', 'Municipio', '1980', '1991', '2000', '2010', '2022']

# Converter as colunas de população para tipo numérico (inteiro)
for year in ['1980', '1991', '2000', '2010', '2022']:
    df_cleaned[year] = pd.to_numeric(df_cleaned[year], errors='coerce')

# Criar diretório para salvar os gráficos
output_dir = 'graficos_declinio_populacao'
os.makedirs(output_dir, exist_ok=True)

# Função para verificar se o município teve declínio populacional
def has_population_decline(data):
    return all(x >= y for x, y in zip(data, data[1:]))

# Função para gerar gráficos de tendência de declínio populacional
def plot_decline_trend(df, municipio):
    # Filtrar os dados para o município selecionado
    data = df[df['Municipio'] == municipio]
    
    # Obter os anos e populações
    anos = ['1980', '1991', '2000', '2010', '2022']
    populacao = data[anos].values.flatten()
    
    # Mostrar os resultados numéricos na tela
    print(f"\nDeclínio populacional para {municipio}:")
    for ano, pop in zip(anos, populacao):
        print(f"{ano}: {pop} habitantes")

    # Criar o gráfico
    plt.figure(figsize=(8, 6))
    plt.plot(anos, populacao, marker='o', linestyle='-', color='r')
    plt.title(f'Declínio Populacional - {municipio}')
    plt.xlabel('Ano')
    plt.ylabel('População')
    plt.grid(True)
    
    # Exibir o gráfico na tela
    plt.show()
    
    # Salvar o gráfico em formato JPG
    output_path = os.path.join(output_dir, f'declinio_{municipio}.jpg')
    plt.savefig(output_path)
    plt.close()

# Identificar os municípios com declínio populacional
municipios_declinio = []
for index, row in df_cleaned.iterrows():
    populacao = row[['1980', '1991', '2000', '2010', '2022']].values
    if has_population_decline(populacao):
        municipios_declinio.append(row['Municipio'])
        plot_decline_trend(df_cleaned, row['Municipio'])

# Exibir o resumo dos municípios com declínio populacional
if municipios_declinio:
    print("\nMunicípios com declínio populacional ao longo do tempo:")
    for municipio in municipios_declinio:
        print(f"- {municipio}")
else:
    print("Nenhum município apresentou declínio populacional ao longo do tempo.")

print(f"\nGráficos gerados e salvos na pasta: {output_dir}")
