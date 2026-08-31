import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configuração de estilo visual dos gráficos
sns.set_theme(style="whitegrid")
plt.rcParams['font.sans-serif'] = 'Arial'

print("--- INICIANDO PROCESSAMENTO DE DADOS NUTRICIONAIS ---")

# 1. Simulação do Dataset de Pacientes Nutricionais
data = {
    'paciente_id': [f'PAC_{i:03d}' for i in range(1, 51)],
    'idade': np.random.randint(18, 65, size=50),
    'genero': np.random.choice(['Feminino', 'Masculino'], size=50, p=[0.6, 0.4]),
    'peso_kg': np.random.normal(72, 12, size=50).round(1),
    'altura_m': np.random.normal(1.68, 0.08, size=50).round(2),
    'objetivo': np.random.choice(['Emagrecimento', 'Hipertrofia', 'Reeducacao'], size=50, p=[0.5, 0.3, 0.2]),
    'adesao_dieta_pct': np.random.randint(40, 100, size=50),
    'perda_peso_kg': np.random.normal(3.5, 1.8, size=50).round(1)
}

df = pd.DataFrame(data)

# 2. Engenharia de Recursos (Feature Engineering) & Métricas
df['imc'] = (df['peso_kg'] / (df['altura_m'] ** 2)).round(1)

def classificar_imc(imc):
    if imc < 18.5: return 'Abaixo do Peso'
    elif 18.5 <= imc < 25: return 'Peso Normal'
    elif 25 <= imc < 30: return 'Sobrepeso'
    else: return 'Obesidade'

df['classificacao_imc'] = df['imc'].apply(classificar_imc)

# 3. Análise Exploratória e Insights de Negócio
print("\n=== RESUMO EXECUTIVO DO CONSULTÓRIO ===")
print(f"Total de Pacientes Analisados: {len(df)}")
print(f"Média de Taxa de Adesão à Dieta: {df['adesao_dieta_pct'].mean():.1f}%")
print(f"Perda de Peso Média por Paciente: {df['perda_peso_kg'].mean():.1f} kg")

print("\n--- Distribuição por Objetivo de Negócio ---")
print(df['objetivo'].value_counts(normalize=True) * 100)

# 4. Geração de Gráficos de Insights
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Gráfico 1: Relação entre Adesão e Perda de Peso
sns.scatterplot(
    data=df, x='adesao_dieta_pct', y='perda_peso_kg', 
    hue='objetivo', style='genero', s=100, ax=axes[0]
)
axes[0].set_title('Impacto da Adesão à Dieta na Perda de Peso', fontsize=12, fontweight='bold')
axes[0].set_xlabel('Taxa de Adesão à Dieta (%)')
axes[0].set_ylabel('Perda de Peso (kg)')

# Gráfico 2: Perfil dos Pacientes por Classificação de IMC
sns.countplot(
    data=df, x='classificacao_imc', palette='Blues_r', 
    order=['Peso Normal', 'Sobrepeso', 'Obesidade'], ax=axes[1]
)
axes[1].set_title('Distribuição de Pacientes por Classificação de IMC', fontsize=12, fontweight='bold')
axes[1].set_xlabel('Classificação do IMC')
axes[1].set_ylabel('Quantidade de Pacientes')

plt.tight_layout()
plt.savefig('relatorio_nutricional_insights.png', dpi=300)
print("\n[SUCESSO] Gráfico 'relatorio_nutricional_insights.png' gerado com sucesso!")