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
- [8. Tree map](#8-tree-map)
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
Campos de JÃºlio
Canabrava do Norte
Carlinda
Colniza
Confresa
Conquista D'Oeste
CotriguaÃ§u
CurvelÃ¢ndia
Feliz Natal
GaÃºcha do Norte
GlÃ³ria D'Oeste
Ipiranga do Norte
ItanhangÃ¡
Lambari D'Oeste
Nova Bandeirantes
Nova Guarita
Nova Lacerda
Nova MarilÃ¢ndia
Nova MaringÃ¡
Nova Monte Verde
Nova NazarÃ©
Nova Santa Helena
Nova UbiratÃ£
Novo Mundo
Novo Santo AntÃ´nio
Planalto da Serra
Pontal do Araguaia
Porto Estrela
QuerÃªncia
RibeirÃ£ozinho
RondolÃ¢ndia
Santa Carmem
Santa Cruz do Xingu
Santa Rita do Trivelato
Santo Afonso
Santo AntÃ´nio do Leverger
SÃ£o José do Povo
SÃ£o José do Xingu
SÃ£o Pedro da Cipa
Sapezal
Serra Nova Dourada
Tabaporã
União do Sul
Vale de Sãoo Domingos

---
# 4. Comparação da população

![Tendências populacionais por Mesorregião](https://github.com/monteiro74/agp/blob/main/analise_comparacao_populacao/f1.png)

![Tendências populacionais por Microrregião](https://github.com/monteiro74/agp/blob/main/analise_comparacao_populacao/f2.png)

![Taxa de crescimento populacional por Mesorregião 2010-2022](https://github.com/monteiro74/agp/blob/main/analise_comparacao_populacao/f3.png)

![Taxa de crescimento populacional por microrregião 2010-2022](https://github.com/monteiro74/agp/blob/main/analise_comparacao_populacao/f4.png)

---
# 5. Análise de tendências dos municípios

![Tendência populaciona Cuiabá](https://github.com/monteiro74/agp/blob/main/analise_tendencia_populacional/graficos_populacao/tendencia_Cuiab%C3%A1.jpg)

Outros municípios podem ser consultados neste [link](https://github.com/monteiro74/agp/tree/main/analise_tendencia_populacional/graficos_populacao).

---
# 6. Análise do declínio populacional

Municípios com declínio populacional ao longo do tempo:
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

![Declínio populacional - Figueirópolis D´Oeste](https://github.com/monteiro74/agp/blob/main/analise_declinio_populacional/f2.png)

![Declínio populacional - Nortelêndia](https://github.com/monteiro74/agp/blob/main/analise_declinio_populacional/f3.png)

![Declínio populacional - Nova Brasilândia](https://github.com/monteiro74/agp/blob/main/analise_declinio_populacional/f4.png)


---
# 7. Distribuição populacional


---
# 8. Tree map


---
# 9. Outras representações gráficas

