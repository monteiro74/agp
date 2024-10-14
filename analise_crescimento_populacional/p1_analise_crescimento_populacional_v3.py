# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14, 2024

@autor: Prof. Dr. Monteiro, E. S.

Prompt:
1. Escreva um programa em python que faça a "Análise de crescimento populacional"
usando o dataset "Populacao_censos_v5.csv"
2. O programa deverá apresentar resultados na saída padrão
3. O programa para adicionar gráficos em cada análise
4. Os gráficos deverão ser adicionados em uma pasta própria em formato .JPG
5. Atenção para registros com valores zero ou nulo.  
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Configuração para melhorar a aparência dos gráficos
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (12, 6)

# Carregar os dados
df = pd.read_csv('Populacao_censos_v5.csv', delimiter=';', encoding='latin1')

# Converter colunas de anos para números
anos = ['1980', '1991', '2000', '2010', '2022']
for ano in anos:
    df[ano] = pd.to_numeric(df[ano], errors='coerce')

# Função para calcular a taxa de crescimento anual
def taxa_crescimento_anual(pop_inicial, pop_final, anos):
    if pop_inicial == 0 or pd.isna(pop_inicial) or pd.isna(pop_final):
        return np.nan
    return (np.power(pop_final / pop_inicial, 1/anos) - 1) * 100

# Calcular taxa de crescimento anual para cada período
periodos = [(1980, 1991), (1991, 2000), (2000, 2010), (2010, 2022)]
for inicio, fim in periodos:
    col_name = f'Taxa_Anual_{inicio}_{fim}'
    anos_periodo = fim - inicio
    df[col_name] = df.apply(lambda row: taxa_crescimento_anual(row[str(inicio)], row[str(fim)], anos_periodo), axis=1)

# Função para imprimir os resultados de crescimento e criar gráfico
def analisar_crescimento(df, col_name, periodo):
    df_valido = df[df[col_name].notna()]
    if df_valido.empty:
        print(f"\nPeríodo {periodo}:")
        print("Não há dados válidos para este período.")
        return

    maior_crescimento = df_valido.loc[df_valido[col_name].idxmax()]
    menor_crescimento = df_valido.loc[df_valido[col_name].idxmin()]

    print(f"\nPeríodo {periodo}:")
    print(f"Município com maior crescimento anual: {maior_crescimento['Municipios']}")
    print(f"Taxa de crescimento anual: {maior_crescimento[col_name]:.2f}%")
    print(f"Município com menor crescimento anual: {menor_crescimento['Municipios']}")
    print(f"Taxa de crescimento anual: {menor_crescimento[col_name]:.2f}%")

    # Criar gráfico de distribuição das taxas de crescimento
    plt.figure(figsize=(12, 6))
    plt.hist(df_valido[col_name], bins=30, edgecolor='black')
    plt.title(f'Distribuição das Taxas de Crescimento Anual - {periodo}')
    plt.xlabel('Taxa de Crescimento Anual (%)')
    plt.ylabel('Frequência')
    plt.axvline(maior_crescimento[col_name], color='r', linestyle='--', label='Maior crescimento')
    plt.axvline(menor_crescimento[col_name], color='g', linestyle='--', label='Menor crescimento')
    plt.legend()
    plt.tight_layout()
    plt.savefig(f'distribuicao_crescimento_{periodo}.png')
    plt.show()

# Analisar crescimento para cada período
for inicio, fim in periodos:
    col_name = f'Taxa_Anual_{inicio}_{fim}'
    analisar_crescimento(df, col_name, f"{inicio}-{fim}")

# Calcular e plotar média de crescimento para o estado
print("\nMédia de crescimento anual para o estado de Mato Grosso:")
medias_crescimento = []
for inicio, fim in periodos:
    col_name = f'Taxa_Anual_{inicio}_{fim}'
    media_crescimento = df[col_name].mean()
    if pd.isna(media_crescimento):
        print(f"Período {inicio}-{fim}: Dados insuficientes para calcular a média")
        medias_crescimento.append(0)
    else:
        print(f"Período {inicio}-{fim}: {media_crescimento:.2f}%")
        medias_crescimento.append(media_crescimento)

# Gráfico de linha para média de crescimento do estado
plt.figure(figsize=(10, 6))
plt.plot([f"{inicio}-{fim}" for inicio, fim in periodos], medias_crescimento, marker='o')
plt.title('Média de Crescimento Anual do Estado de Mato Grosso')
plt.xlabel('Período')
plt.ylabel('Taxa de Crescimento Anual Média (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('media_crescimento_estado.png')
plt.show()

# Identificar municípios com crescimento consistentemente acima da média
colunas_taxa = [f'Taxa_Anual_{inicio}_{fim}' for inicio, fim in periodos]
medias = df[colunas_taxa].mean()
crescimento_acima_media = df[df[colunas_taxa].gt(medias).all(axis=1)]

print(f"\nMunicípios com crescimento consistentemente acima da média em todos os períodos:")
if crescimento_acima_media.empty:
    print("Nenhum município apresentou crescimento acima da média em todos os períodos.")
else:
    for municipio in crescimento_acima_media['Municipios']:
        print(municipio)

    # Gráfico de barras para municípios com crescimento acima da média
    plt.figure(figsize=(12, 6))
    crescimento_acima_media[colunas_taxa].T.plot(kind='bar')
    plt.title('Taxas de Crescimento dos Municípios Acima da Média')
    plt.xlabel('Período')
    plt.ylabel('Taxa de Crescimento Anual (%)')
    plt.legend(crescimento_acima_media['Municipios'], bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig('municipios_acima_media.png')
    plt.show()

# Análise adicional: Identificar municípios que passaram a existir após 1980
novos_municipios = df[df['1980'] == 0]['Municipios']
print(f"\nMunicípios que passaram a existir após 1980:")
for municipio in novos_municipios:
    print(municipio)

# Gráfico de evolução populacional para novos municípios
plt.figure(figsize=(12, 6))
for municipio in novos_municipios:
    dados_municipio = df[df['Municipios'] == municipio][anos].iloc[0]
    plt.plot(anos, dados_municipio, marker='o', label=municipio)

plt.title('Evolução Populacional dos Novos Municípios')
plt.xlabel('Ano')
plt.ylabel('População')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('evolucao_novos_municipios.png')
plt.show()