# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 2024

@author: Prof. Dr. Monteiro, E. S.

Prompt:
Gere um programa em python que use o dataset "Populacao_censos_v5.csv"
Faça uma análise da distribuição populacional, indicando: 
    a) Analisar como a população do estado está distribuída entre os municípios e, 
    b) Calcular medidas de concentração populacional.
Mostre os resultados na saída padrão (tela) com textos e gráficos.
Grave os gráficos gerados em arquivos JPG.
"""
import pandas as pd
import numpy as np
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
output_dir = 'graficos_distribuicao_populacao'
os.makedirs(output_dir, exist_ok=True)

# Função para calcular a concentração populacional usando o coeficiente de Gini
def calc_gini(population):
    # Remover valores nulos e ordenar a população
    population = population[~np.isnan(population)]
    sorted_pop = np.sort(population)
    n = len(sorted_pop)
    
    # Gini é calculado pela fórmula padrão
    cumulative_pop = np.cumsum(sorted_pop)
    relative_pop = cumulative_pop / cumulative_pop[-1]  # normaliza pelo total da população
    
    # Calcular a área da curva de Lorenz
    lorenz_curve_area = np.sum(relative_pop[:-1]) / n
    
    # Gini é a razão entre a área sob a linha de igualdade e a curva de Lorenz
    gini_index = 1 - 2 * lorenz_curve_area
    
    return gini_index

# Função para gerar gráficos de distribuição populacional
def plot_population_distribution(df, estado, year):
    # Filtrar os dados para o estado selecionado e o ano
    data = df[df['Estado'] == estado]
    municipios = data['Municipio']
    populacao = data[year].values
    
    # Calcular proporção populacional
    total_pop = np.nansum(populacao)  # Considerar NaNs
    proporcao_pop = (populacao / total_pop) * 100
    
    # Exibir proporção populacional na tela
    print(f"\nDistribuição populacional no estado {estado} em {year}:")
    for municipio, prop in zip(municipios, proporcao_pop):
        print(f"{municipio}: {prop:.2f}% da população do estado")
    
    # Calcular o índice de Gini (concentração populacional)
    gini_index = calc_gini(populacao)
    print(f"\nÍndice de Gini para {estado} em {year}: {gini_index:.4f}")
    
    # Criar gráfico de pizza para a distribuição populacional
    plt.figure(figsize=(8, 6))
    plt.pie(proporcao_pop, labels=municipios, autopct='%1.1f%%', startangle=90)
    plt.title(f'Distribuição Populacional - {estado} ({year})')
    
    # Salvar o gráfico em formato JPG
    output_path = os.path.join(output_dir, f'distribuicao_{estado}_{year}.jpg')
    plt.savefig(output_path, format='jpg')
    
    # Exibir o gráfico na tela
    plt.show()
    plt.close()

# Analisar a distribuição populacional para cada estado e ano de interesse
anos_interesse = ['1980', '1991', '2000', '2010', '2022']
estados = df_cleaned['Estado'].unique()

for estado in estados:
    for ano in anos_interesse:
        plot_population_distribution(df_cleaned, estado, ano)

print(f"\nGráficos de distribuição gerados e salvos na pasta: {output_dir}")
