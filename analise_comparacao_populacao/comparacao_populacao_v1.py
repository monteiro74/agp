# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14, 2024

@author: Prof. Dr. Monteiro, E. S.
    
Prompt:
1. Escreva um programa em python que faça a "Comparação regional", 
usando o dataset "Populacao_censos_v5.csv", incluindo: 
    A) Analisar tendências populacionais por mesorregião e microrregião e 
    B) Comparar o desenvolvimento populacional de diferentes regiões do estado. 
2. O programa deverá apresentar resultados na saída padrão
3. O programa para adicionar gráficos em cada análise
4. Os gráficos deverão ser adicionados em uma pasta própria em formato .JPG
5. Atenção para registros com valores zero ou nulo.     
"""

import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict

# Carregar os dados
df = pd.read_csv('Populacao_censos_v5.csv', sep=';', encoding='latin1')

# Converter colunas de anos para números, tratando zeros como NaN
for year in ['1980', '1991', '2000', '2010', '2022']:
    df[year] = pd.to_numeric(df[year], errors='coerce')

# Função para calcular a taxa de crescimento
def calculate_growth_rate(start_value, end_value, years):
    if pd.isna(start_value) or pd.isna(end_value) or start_value == 0:
        return None
    return (end_value / start_value) ** (1 / years) - 1

# Análise por mesorregião
def analyze_mesoregion():
    mesoregion_data = defaultdict(lambda: defaultdict(list))
    
    for _, row in df.iterrows():
        mesoregion = row['Mesorregiao']
        for year in ['1980', '1991', '2000', '2010', '2022']:
            if not pd.isna(row[year]):
                mesoregion_data[mesoregion][year].append(row[year])
    
    results = {}
    for mesoregion, data in mesoregion_data.items():
        results[mesoregion] = {
            'population': {year: sum(values) for year, values in data.items()},
            'growth_rate': {}
        }
        
        for i in range(len(['1980', '1991', '2000', '2010', '2022']) - 1):
            start_year = ['1980', '1991', '2000', '2010', '2022'][i]
            end_year = ['1980', '1991', '2000', '2010', '2022'][i+1]
            start_value = results[mesoregion]['population'][start_year]
            end_value = results[mesoregion]['population'][end_year]
            years = int(end_year) - int(start_year)
            growth_rate = calculate_growth_rate(start_value, end_value, years)
            results[mesoregion]['growth_rate'][f'{start_year}-{end_year}'] = growth_rate
    
    return results

# Análise por microrregião
def analyze_microregion():
    microregion_data = defaultdict(lambda: defaultdict(list))
    
    for _, row in df.iterrows():
        microregion = row['Microrregiao']
        for year in ['1980', '1991', '2000', '2010', '2022']:
            if not pd.isna(row[year]):
                microregion_data[microregion][year].append(row[year])
    
    results = {}
    for microregion, data in microregion_data.items():
        results[microregion] = {
            'population': {year: sum(values) for year, values in data.items()},
            'growth_rate': {}
        }
        
        for i in range(len(['1980', '1991', '2000', '2010', '2022']) - 1):
            start_year = ['1980', '1991', '2000', '2010', '2022'][i]
            end_year = ['1980', '1991', '2000', '2010', '2022'][i+1]
            start_value = results[microregion]['population'][start_year]
            end_value = results[microregion]['population'][end_year]
            years = int(end_year) - int(start_year)
            growth_rate = calculate_growth_rate(start_value, end_value, years)
            results[microregion]['growth_rate'][f'{start_year}-{end_year}'] = growth_rate
    
    return results

# Visualização das tendências populacionais
def plot_population_trends(data, title):
    plt.figure(figsize=(12, 6))
    for region, values in data.items():
        years = [1980, 1991, 2000, 2010, 2022]
        population = [values['population'][str(year)] for year in years]
        plt.plot(years, population, marker='o', label=region)
    
    plt.title(f'Tendências Populacionais por {title}')
    plt.xlabel('Ano')
    plt.ylabel('População')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()

# Comparação do desenvolvimento populacional
def compare_regions(data, title):
    growth_rates = {region: values['growth_rate']['2010-2022'] for region, values in data.items()}
    growth_rates = {k: v for k, v in growth_rates.items() if v is not None}
    
    sorted_regions = sorted(growth_rates.items(), key=lambda x: x[1], reverse=True)
    
    plt.figure(figsize=(12, 6))
    plt.bar([region for region, _ in sorted_regions], [rate for _, rate in sorted_regions])
    plt.title(f'Taxa de Crescimento Populacional por {title} (2010-2022)')
    plt.xlabel(title)
    plt.ylabel('Taxa de Crescimento Anual')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

# Executar análises
mesoregion_results = analyze_mesoregion()
microregion_results = analyze_microregion()

# Visualizar resultados
plot_population_trends(mesoregion_results, 'Mesorregião')
plot_population_trends(microregion_results, 'Microrregião')
compare_regions(mesoregion_results, 'Mesorregião')
compare_regions(microregion_results, 'Microrregião')

# Imprimir resultados detalhados
print("Análise por Mesorregião:")
for mesoregion, data in mesoregion_results.items():
    print(f"\n{mesoregion}:")
    print("População:")
    for year, pop in data['population'].items():
        print(f"  {year}: {pop:,}")
    print("Taxa de Crescimento:")
    for period, rate in data['growth_rate'].items():
        if rate is not None:
            print(f"  {period}: {rate:.2%}")
        else:
            print(f"  {period}: N/A")

print("\nAnálise por Microrregião:")
for microregion, data in microregion_results.items():
    print(f"\n{microregion}:")
    print("População:")
    for year, pop in data['population'].items():
        print(f"  {year}: {pop:,}")
    print("Taxa de Crescimento:")
    for period, rate in data['growth_rate'].items():
        if rate is not None:
            print(f"  {period}: {rate:.2%}")
        else:
            print(f"  {period}: N/A")