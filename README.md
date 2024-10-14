# Projeto AGP
Análise gráfica populacional

Autor: Prof. Dr. **Monteiro, E. S**.
Ano: 2024.


---

- [Projeto AGP](#projeto-agp)
- [1. Descrição do dataset](#1-descrição-do-dataset)
- [2. Metodologia](#2-metodologia)
- [3. Análise populacional](#3-análise-populacional)
- [4. Comparação da população](#4-comparação-da-população)
- [5. Análise de tendências dos municípios](#5-análise-de-tendências-dos-municípios)
- [6. Análise do declínio populacional](#6-análise-do-declínio-populacional)
- [7. Distribuição populacional](#7-distribuição-populacional)
- [8. Tree map e heat map](#8-tree-map-e-heat-map)
- [9. Outras representações gráficas](#9-outras-representações-gráficas)


---
# 1. Descrição do dataset

Arquivo CSV
População de Mato Gross (MT) por municípios de 1980 a 2022
Fonte: [IBGE, censo populacional](https://www.ibge.gov.br/estatisticas/sociais/populacao.html).

---
# 2. Metodologia

1. Obtenção do dataset em formato CSV, formatação do dataset (tabela) com os dados para os respectivos anos no site do IBGE.
2. Criar prompts em linguagem natural para que as IAs generativas possam produzir programas em Python.
3. Submeter cada prompt e respectivo arquivo do dataset em format CSV para as IA generativas. 
4. Utilizar as IAs: Claude e ChatGPT com os prompts e dataset.
5. Executar cada programa python dentro da IDE Spyder.
6. Analisar os resultados das saídas dos programas.
7. Cada programa Python deve gerar resultados na tela (saída padrão) e na forma de gráficos em formato JPG. 
8. Outras visualizações foram geradas com Power BI.
9. Montar um repositório público com os dados gerados.

---
# 3. Análise populacional

Período 1980-1991:
Município com maior crescimento anual: Guarantã do Norte
Taxa de crescimento anual: 40.36%
Município com menor crescimento anual: Jangada
Taxa de crescimento anual: -17.69%

Período 2000-2010:
Município com maior crescimento anual: Lucas do Rio Verde
Taxa de crescimento anual: 8.96%
Município com menor crescimento anual: Itaúba
Taxa de crescimento anual: -6.08%

Período 2010-2022:
Município com maior crescimento anual: Santa Rita do Trivelato
Taxa de crescimento anual: 17.83%
Município com menor crescimento anual: Santo Antônio do Leverger
Taxa de crescimento anual: -14.91%

Média de crescimento anual para o estado de Mato Grosso:
Período 1980-1991: 6.59%
Período 1991-2000: -0.51%
Período 2000-2010: 1.26%
Período 2010-2022: 0.85%

Municípios com crescimento consistentemente acima da média em todos os períodos:
Agua Boa
Brasnorte
Campo Novo do Parecis
Campo Verde
Canarana
Lucas do Rio Verde
Matupá
Sinop
Sorriso


![Média de crescimento anual do Estado de Mato Grosso](https://github.com/monteiro74/agp/blob/main/analise_crescimento_populacional/media_crescimento_estado.png)

Municípios com crescimento consistentemente acima da média em todos os períodos:
Agua Boa
Brasnorte
Campo Novo do Parecis
Campo Verde
Canarana
Lucas do Rio Verde
Matupá
Sinop
Sorriso

![Taxa de crescimento dos municípios acima da média](https://github.com/monteiro74/agp/blob/main/analise_crescimento_populacional/municipios_acima_media.png)

Municípios que passaram a existir após 1980:
Alto Boa Vista
Bom Jesus do Araguaia
Campos de Júlio
Canabrava do Norte
Carlinda
Colniza
Confresa
Conquista D'Oeste
Cotriguaçu
Curvelândia
Feliz Natal
Gaúcha do Norte
Glória D'Oeste
Ipiranga do Norte
Itanhangá
Lambari D'Oeste
Nova Bandeirantes
Nova Guarita
Nova Lacerda
Nova Marilândia
Nova Maringá
Nova Monte Verde
Nova Nazaré
Nova Santa Helena
Nova Ubiratã
Novo Mundo
Novo Santo Antônio
Planalto da Serra
Pontal do Araguaia
Porto Estrela
Querência
Ribeirãozinho
Rondolândia
Santa Carmem
Santa Cruz do Xingu
Santa Rita do Trivelato
Santo Afonso
Santo Antônio do Leverger
São José do Povo
São José do Xingu
São Pedro da Cipa
Sapezal
Serra Nova Dourada
Tabaporã
União do Sul
Vale de Sãoo Domingos

[Início](#projeto-agp)

---
# 4. Comparação da população

![Tendências populacionais por Mesorregião](https://github.com/monteiro74/agp/blob/main/analise_comparacao_populacao/f1.png)

![Tendências populacionais por Microrregião](https://github.com/monteiro74/agp/blob/main/analise_comparacao_populacao/f2.png)

![Taxa de crescimento populacional por Mesorregião 2010-2022](https://github.com/monteiro74/agp/blob/main/analise_comparacao_populacao/f3.png)

![Taxa de crescimento populacional por microrregião 2010-2022](https://github.com/monteiro74/agp/blob/main/analise_comparacao_populacao/f4.png)

[Início](#projeto-agp)

---
# 5. Análise de tendências dos municípios

Exemplo: 

![Tendência populaciona Cuiabá](https://github.com/monteiro74/agp/blob/main/analise_tendencia_populacional/graficos_populacao/tendencia_Cuiab%C3%A1.jpg)

Outros municípios podem ser consultados neste [link](https://github.com/monteiro74/agp/tree/main/analise_tendencia_populacional/graficos_populacao).

[Início](#projeto-agp)

---
# 6. Análise do declínio populacional

Alguns municípios com declínio populacional ao longo do tempo:
- Dom Aquino
- Figueirópolis D'Oeste
- Nortelândia
- Nova Brasilândia

Declínio populacional para Dom Aquino:
1980: 11329 habitantes
1991: 8943 habitantes
2000: 8418 habitantes
2010: 8171 habitantes
2022: 7872 habitantes

![Declínio populacional - Don Aquino](https://github.com/monteiro74/agp/blob/main/analise_declinio_populacional/f1.png)

Declínio populacional para Figueirópolis D'Oeste:
1980: 7076 habitantes
1991: 5407 habitantes
2000: 4315 habitantes
2010: 3796 habitantes
2022: 3187 habitantes


![Declínio populacional - Figueirópolis D´Oeste](https://github.com/monteiro74/agp/blob/main/analise_declinio_populacional/f2.png)


Declínio populacional para Nortelândia:
1980: 10447 habitantes
1991: 10038 habitantes
2000: 7246 habitantes
2010: 6436 habitantes
2022: 5956 habitantes


![Declínio populacional - Nortelêndia](https://github.com/monteiro74/agp/blob/main/analise_declinio_populacional/f3.png)

Declínio populacional para Nova Brasilândia:
1980: 11495 habitantes
1991: 9611 habitantes
2000: 5786 habitantes
2010: 4587 habitantes
2022: 4200 habitantes


![Declínio populacional - Nova Brasilândia](https://github.com/monteiro74/agp/blob/main/analise_declinio_populacional/f4.png)

[Início](#projeto-agp)

---
# 7. Distribuição populacional

![Distribuição populacional MT 1980](https://github.com/monteiro74/agp/blob/main/analise_distribuicao_populacao/distribuicao_MT_1980.jpg)


Índice de Gini para MT em 1991: 0.7246

![Distribuição populacional MT 1991](https://github.com/monteiro74/agp/blob/main/analise_distribuicao_populacao/distribuicao_MT_1991.jpg)

Distribuição populacional no estado MT em 2000:
* Acorizal: 0.23% da população do estado
* Agua Boa: 0.67% da população do estado
* Alta Floresta: 1.88% da população do estado
* Alto Araguaia: 0.46% da população do estado
* Alto Boa Vista: 0.25% da população do estado
* Alto Garças: 0.33% da população do estado
* Alto Paraguai: 0.34% da população do estado
* Alto Taquari: 0.18% da população do estado
* Apiacás: 0.27% da população do estado
* Araguaiana: 0.14% da população do estado
* Araguainha: 0.05% da população do estado
* Araputanga: 0.55% da população do estado
* Arenápolis: 0.46% da população do estado
* Aripuanã: 1.10% da população do estado
* Barão de Melgaço: 0.31% da população do estado
* Barra do Bugres: 1.10% da população do estado
* Barra do Garças: 2.08% da população do estado
* Bom Jesus do Araguaia: 0.00% da população do estado
* Brasnorte: 0.39% da população do estado
* Cáceres: 3.43% da população do estado
* Campinápolis: 0.50% da população do estado
* Campo Novo do Parecis: 0.70% da população do estado
* Campo Verde: 0.69% da população do estado
* Campos de Júlio: 0.12% da população do estado
* Canabrava do Norte: 0.20% da população do estado
* Canarana: 0.62% da população do estado
* Carlinda: 0.49% da população do estado
* Castanheira: 0.31% da população do estado
* Chapada dos Guimarães: 0.63% da população do estado
* Cláudia: 0.41% da população do estado
* Cocalinho: 0.22% da população do estado
* Colíder: 1.12% da população do estado
* Colniza: 0.00% da população do estado
* Comodoro: 0.60% da população do estado
* Confresa: 0.71% da população do estado
* Conquista D'Oeste: 0.00% da população do estado
* Cotriguaçu: 0.34% da população do estado
* Cuiabá: 19.30% da população do estado
* Curvelândia: 0.00% da população do estado
* Denise: 0.30% da população do estado
* Diamantino: 0.74% da população do estado
* Dom Aquino: 0.34% da população do estado
* Feliz Natal: 0.27% da população do estado
* Figueirópolis D'Oeste: 0.17% da população do estado
* Gaúcha do Norte: 0.18% da população do estado
* General Carneiro: 0.17% da população do estado
* Glória D'Oeste: 0.13% da população do estado
* Guarantã do Norte: 1.13% da população do estado
* Guiratinga: 0.50% da população do estado
* Indiavaí: 0.08% da população do estado
* Ipiranga do Norte: 0.00% da população do estado
* Itanhangá: 0.00% da população do estado
* Itaúba: 0.34% da população do estado
* Itiquira: 0.37% da população do estado
* Jaciara: 0.95% da população do estado
* Jangada: 0.28% da população do estado
* Jauru: 0.51% da população do estado
* Juara: 1.23% da população do estado
* Juína: 1.52% da população do estado
* Juruena: 0.22% da população do estado
* Juscimeira: 0.48% da população do estado
* Lambari D'Oeste: 0.19% da população do estado
* Lucas do Rio Verde: 0.77% da população do estado
* Luciara: 0.10% da população do estado
* Marcelândia: 0.58% da população do estado
* Matupá: 0.45% da população do estado
* Mirassol D'Oeste: 0.92% da população do estado
* Nobres: 0.60% da população do estado
* Nortelândia: 0.29% da população do estado
* Nossa Senhora do Livramento: 0.48% da população do estado
* Nova Bandeirantes: 0.28% da população do estado
* Nova Brasilândia: 0.23% da população do estado
* Nova Canaã do Norte: 0.46% da população do estado
* Nova Guarita: 0.23% da população do estado
* Nova Lacerda: 0.16% da população do estado
* Nova Marilândia: 0.09% da população do estado
* Nova Maringá: 0.16% da população do estado
* Nova Monte Verde: 0.27% da população do estado
* Nova Mutum: 0.59% da população do estado
* Nova Nazaré: 0.00% da população do estado
* Nova Olímpia: 0.57% da população do estado
* Nova Santa Helena: 0.00% da população do estado
* Nova Ubiratã: 0.23% da população do estado
* Nova Xavantina: 0.71% da população do estado
* Novo Horizonte do Norte: 0.14% da população do estado
* Novo Mundo: 0.20% da população do estado
* Novo Santo Antônio: 0.00% da população do estado
* Novo São Joaquim: 0.38% da população do estado
* Paranaíta: 0.41% da população do estado
* Paranatinga: 0.61% da população do estado
* Pedra Preta: 0.54% da população do estado
* Peixoto de Azevedo: 1.04% da população do estado
* Planalto da Serra: 0.12% da população do estado
* Poconé: 1.23% da população do estado
* Pontal do Araguaia: 0.15% da população do estado
* Ponte Branca: 0.08% da população do estado
* Pontes e Lacerda: 1.72% da população do estado
* Porto Alegre do Norte: 0.34% da população do estado
* Porto dos Gaúchos: 0.23% da população do estado
* Porto Esperidião: 0.40% da população do estado
* Porto Estrela: 0.19% da população do estado
* Poxoréo: 0.80% da população do estado
* Primavera do Leste: 1.59% da população do estado
* Querência: 0.29% da população do estado
* Reserva do Cabaçal: 0.10% da população do estado
* Ribeirão Cascalheira: 0.35% da população do estado
* Ribeirãozinho: 0.08% da população do estado
* Rio Branco: 0.20% da população do estado
* Rondolândia: 0.00% da população do estado
* Rondonópolis: 6.00% da população do estado
* Rosário Oeste: 0.75% da população do estado
* Salto do Céu: 0.19% da população do estado
* Santa Carmem: 0.14% da população do estado
* Santa Cruz do Xingu: 0.00% da população do estado
* Santa Rita do Trivelato: 0.00% da população do estado
* Santa Terezinha: 0.25% da população do estado
* Santo Afonso: 0.12% da população do estado
* Santo Antônio do Leste: 0.00% da população do estado
* Santo Antônio do Leverger: 0.62% da população do estado
* São Félix do Araguaia: 0.43% da população do estado
* São José do Povo: 0.12% da população do estado
* São José do Rio Claro: 0.51% da população do estado
* São José do Xingu: 0.24% da população do estado
* São José dos Quatro Marcos: 0.79% da população do estado
* São Pedro da Cipa: 0.14% da população do estado
* Sapezal: 0.31% da população do estado
* Serra Nova Dourada: 0.00% da população do estado
* Sinop: 2.99% da população do estado
* Sorriso: 1.42% da população do estado
* Tabaporã: 0.43% da população do estado
* Tangará da Serra: 2.35% da população do estado
* Tapurah: 0.46% da população do estado
* Terra Nova do Norte: 0.55% da população do estado
* Tesouro: 0.12% da população do estado
* Torixoréu: 0.19% da população do estado
* União do Sul: 0.17% da população do estado
* Vale de São Domingos: 0.00% da população do estado
* Várzea Grande: 8.60% da população do estado
* Vera: 0.36% da população do estado
* Vila Bela da Santíssima Trindade: 0.51% da população do estado
* Vila Rica: 0.62% da população do estado

Índice de Gini para MT em 2000: 0.6597

[Início](#projeto-agp)

![Distribuição populacional MT 2000](https://github.com/monteiro74/agp/blob/main/analise_distribuicao_populacao/distribuicao_MT_2000.jpg)


Índice de Gini para MT em 2010: 0.6447


![Distribuição populacional MT 2010](https://github.com/monteiro74/agp/blob/main/analise_distribuicao_populacao/distribuicao_MT_2010.jpg)

Distribuição populacional no estado MT em 2022:
Acorizal: 0.14% da população do estado
Agua Boa: 0.80% da população do estado
Alta Floresta: 1.60% da população do estado
Alto Araguaia: 0.47% da população do estado
Alto Boa Vista: 0.15% da população do estado
Alto Garças: 0.36% da população do estado
Alto Paraguai: 0.22% da população do estado
Alto Taquari: 0.30% da população do estado
Apiacás: 0.23% da população do estado
Araguaiana: 0.10% da população do estado
Araguainha: 0.03% da população do estado
Araputanga: 0.40% da população do estado
Arenápolis: 0.29% da população do estado
Aripuanã: 0.67% da população do estado
Barão de Melgaço: 0.20% da população do estado
Barra do Bugres: 0.80% da população do estado
Barra do Garças: 1.89% da população do estado
Bom Jesus do Araguaia: 0.20% da população do estado
Brasnorte: 0.46% da população do estado
Cáceres: 2.45% da população do estado
Campinápolis: 0.42% da população do estado
Campo Novo do Parecis: 1.25% da população do estado
Campo Verde: 1.22% da população do estado
Campos de Júlio: 0.24% da população do estado
Canabrava do Norte: 0.12% da população do estado
Canarana: 0.71% da população do estado
Carlinda: 0.28% da população do estado
Castanheira: 0.21% da população do estado
Chapada dos Guimarães: 0.52% da população do estado
Cláudia: 0.26% da população do estado
Cocalinho: 0.17% da população do estado
Colíder: 0.86% da população do estado
Colniza: 0.70% da população do estado
Comodoro: 0.50% da população do estado
Confresa: 0.96% da população do estado
Conquista D'Oeste: 0.10% da população do estado
Cotriguaçu: 0.30% da população do estado
Cuiabá: 17.79% da população do estado
Curvelândia: 0.13% da população do estado
Denise: 0.19% da população do estado
Diamantino: 0.60% da população do estado
Dom Aquino: 0.22% da população do estado
Feliz Natal: 0.29% da população do estado
Figueirópolis D'Oeste: 0.09% da população do estado
Gaúcha do Norte: 0.24% da população do estado
General Carneiro: 0.16% da população do estado
Glória D'Oeste: 0.08% da população do estado
Guarantã do Norte: 0.85% da população do estado
Guiratinga: 0.30% da população do estado
Indiavaí: 0.06% da população do estado
Ipiranga do Norte: 0.21% da população do estado
Itanhangá: 0.21% da população do estado
Itaúba: 0.14% da população do estado
Itiquira: 0.33% da população do estado
Jaciara: 0.78% da população do estado
Jangada: 0.20% da população do estado
Jauru: 0.23% da população do estado
Juara: 0.95% da população do estado
Juína: 1.25% da população do estado
Juruena: 0.28% da população do estado
Juscimeira: 0.31% da população do estado
Lambari D'Oeste: 0.13% da população do estado
Lucas do Rio Verde: 2.29% da população do estado
Luciara: 0.07% da população do estado
Marcelândia: 0.31% da população do estado
Matupá: 0.55% da população do estado
Mirassol D'Oeste: 0.73% da população do estado
Nobres: 0.42% da população do estado
Nortelândia: 0.16% da população do estado
Nossa Senhora do Livramento: 0.35% da população do estado
Nova Bandeirantes: 0.37% da população do estado
Nova Brasilândia: 0.11% da população do estado
Nova Canaã do Norte: 0.18% da população do estado
Nova Guarita: 0.12% da população do estado
Nova Lacerda: 0.11% da população do estado
Nova Marilândia: 0.32% da população do estado
Nova Maringá: 0.13% da população do estado
Nova Monte Verde: 0.10% da população do estado
Nova Mutum: 0.16% da população do estado
Nova Nazaré: 0.23% da população do estado
Nova Olímpia: 1.52% da população do estado
Nova Santa Helena: 0.45% da população do estado
Nova Ubiratã: 0.31% da população do estado
Nova Xavantina: 0.67% da população do estado
Novo Horizonte do Norte: 0.18% da população do estado
Novo Mundo: 0.09% da população do estado
Novo Santo Antônio: 0.19% da população do estado
Novo São Joaquim: 0.06% da população do estado
Paranaíta: 0.32% da população do estado
Paranatinga: 0.72% da população do estado
Pedra Preta: 0.49% da população do estado
Peixoto de Azevedo: 0.89% da população do estado
Planalto da Serra: 0.09% da população do estado
Poconé: 0.85% da população do estado
Pontal do Araguaia: 0.19% da população do estado
Ponte Branca: 0.05% da população do estado
Pontes e Lacerda: 1.42% da população do estado
Porto Alegre do Norte: 0.38% da população do estado
Porto dos Gaúchos: 0.15% da população do estado
Porto Esperidião: 0.28% da população do estado
Porto Estrela: 0.09% da população do estado
Poxoréo: 0.64% da população do estado
Primavera do Leste: 2.33% da população do estado
Querência: 0.73% da população do estado
Reserva do Cabaçal: 0.06% da população do estado
Ribeirão Cascalheira: 0.27% da população do estado
Ribeirãozinho: 0.07% da população do estado
Rio Branco: 0.12% da população do estado
Rondolândia: 0.10% da população do estado
Rondonópolis: 6.69% da população do estado
Rosário Oeste: 0.42% da população do estado
Salto do Céu: 0.15% da população do estado
Santa Carmem: 0.07% da população do estado
Santa Cruz do Xingu: 0.08% da população do estado
Santa Rita do Trivelato: 0.49% da população do estado
Santa Terezinha: 0.41% da população do estado
Santo Afonso: 0.16% da população do estado
Santo Antônio do Leste: 0.11% da população do estado
Santo Antônio do Leverger: 0.07% da população do estado
São Félix do Araguaia: 0.10% da população do estado
São José do Povo: 0.09% da população do estado
São José do Rio Claro: 0.21% da população do estado
São José do Xingu: 0.11% da população do estado
São José dos Quatro Marcos: 0.42% da população do estado
São Pedro da Cipa: 0.37% da população do estado
Sapezal: 0.79% da população do estado
Serra Nova Dourada: 0.05% da população do estado
Sinop: 5.36% da população do estado
Sorriso: 3.02% da população do estado
Tabaporã: 0.27% da população do estado
Tangará da Serra: 2.91% da população do estado
Tapurah: 0.39% da população do estado
Terra Nova do Norte: 0.29% da população do estado
Tesouro: 0.08% da população do estado
Torixoréu: 0.11% da população do estado
União do Sul: 0.10% da população do estado
Vale de São Domingos: 0.08% da população do estado
Várzea Grande: 8.18% da população do estado
Vera: 0.35% da população do estado
Vila Bela da Santíssima Trindade: 0.46% da população do estado
Vila Rica: 0.54% da população do estado

Índice de Gini para MT em 2022: 0.6776

![Distribuição populacional MT 2022](https://github.com/monteiro74/agp/blob/main/analise_distribuicao_populacao/distribuicao_MT_2022.jpg)

[Início](#projeto-agp)

---
# 8. Tree map e heat map

![Tree map da população MT 2022](https://github.com/monteiro74/agp/blob/main/mapa_de_calor/treemap_populacao_municipios.jpg)

![Heat map](https://github.com/monteiro74/agp/blob/main/mapa_de_calor/heatmap_populacao_municipios.jpg)

[Início](#projeto-agp)

---
# 9. Outras representações gráficas

![gráfico1](https://github.com/monteiro74/agp/blob/main/outras_rep_graficas/grafico_1.png)

![gráfico2](https://github.com/monteiro74/agp/blob/main/outras_rep_graficas/mapa_1.png)

[Início](#projeto-agp)
