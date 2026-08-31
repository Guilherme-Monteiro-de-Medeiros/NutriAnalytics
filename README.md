# 🥗 NutriAnalytics — Inteligência de Dados & Prescrição Nutricional

O **NutriAnalytics** é uma solução integrada desenvolvida para a análise de dados clínicos e automação de prescrições nutricionais personalizadas. O projeto combina processamento analítico em Python com um Dashboard Web interativo para suporte à tomada de decisão clínica.

---

## 🚀 Funcionalidades da Aplicação Web (`index.html`)

- **Cálculo Metabólico de Precisão:** Aplicação da equação de *Harris-Benedict* ajustada ao nível de atividade física do paciente (Sedentário, Leve/Moderado e Hipertrofia/Intenso).
- **Gerador de Cardápios Semanal Inteligente:**
  - Prescrição individualizada de Segunda a Domingo com variação em todas as 4 refeições diárias.
  - Alimentos baseados no banco de dados **TACO (Tabela Brasileira de Composição de Alimentos)**.
  - Equivalência prática em **porções e medidas caseiras** (ex: colheres de sopa, fatias, unidades e gramas).
  - Nutrição focada em comida sólida e acessível (sem dependência de suplementos).
- **Cálculo de Meta Hídrica:** Automatizado na regra clínica de 35 ml/kg/dia.
- **Visualização de Dados em Tempo Real:** Gráficos interativos renderizados via *Chart.js* para acompanhamento da distribuição de macronutrientes (Proteínas, Carboidratos e Gorduras).

---

## 🐍 Análise de Dados com Python (`analise_nutricional.py`)

O repositório também conta com um pipeline de dados em Python voltado para a análise de acompanhamento do paciente:

1. **Processamento e Modelagem:** Avaliação de métricas nutricionais ao longo do tempo.
2. **Geração de Insights Visuais:** Exportação automática do relatório visual `relatorio_nutricional_insights.png` integrado ao dashboard.

---

## 🛠️ Tecnologias Utilizadas

- **Front-end / Dashboard:** HTML5, CSS3 Moderno (CSS Variables, Flexbox, CSS Grid) e JavaScript puro (Vanilla JS).
- **Data Viz Web:** [Chart.js](https://www.chart.js.org/) via CDN.
- **Data Science / Back-end:** Python 3 (Pandas, Matplotlib, Seaborn).

---

## 📂 Como Executar o Projeto

1. Clone este repositório:
```bash
git clone https://github.com/Guilherme-Monteiro-de-Medeiros/NutriAnalytics.git
```

2. **Para a Interface Web:** Abra o arquivo `index.html` em qualquer navegador web moderno.
3. **Para a Análise em Python:** Execute o script `analise_nutricional.py` no seu ambiente Python.
