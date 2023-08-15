import basedosdados as bd

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind


# código dado no site https://basedosdados.org/dataset/96eab476-5d30-459b-82be-f888d4d0d6b9?table=bc84dea9-1126-4423-86d2-8835e6b19a72
df = bd.read_table(dataset_id='br_inep_ideb',
table_id='brasil',
billing_project_id="education-ufrj-analytica") #script foi testado no google-colab


fundamental_municipais = df[(df['ensino'] == 'fundamental') & (df['rede'] == 'municipal')]
fundamental_estaduais = df[(df['ensino'] == 'fundamental') & (df['rede'] == 'estadual')]

t_statistic, p_value = ttest_ind(fundamental_municipais['nota_saeb_media_padronizada'], fundamental_estaduais['nota_saeb_media_padronizada'])
print("Questão 1:")
print(f"T-Statistic: {t_statistic}")
print(f"P-Value: {p_value}")

sns.boxplot(x='rede', y='nota_saeb_media_padronizada', data=df[df['ensino'] == 'fundamental'])
plt.title('Desempenho acadêmico nas escolas municipais vs estaduais na educação fundamental')
plt.show()

fundamental_privadas = df[(df['ensino'] == 'fundamental') & (df['rede'] == 'privada')]
fundamental_publicas = df[(df['ensino'] == 'fundamental') & ((df['rede'] == 'municipal') | (df['rede'] == 'estadual'))]#

t_statistic, p_value = ttest_ind(fundamental_privadas['nota_saeb_media_padronizada'], fundamental_publicas['nota_saeb_media_padronizada'])
print("\nQuestão 2:")
print(f"T-Statistic: {t_statistic}")
print(f"P-Value: {p_value}")

sns.boxplot(x='rede', y='nota_saeb_media_padronizada', data=df[df['ensino'] == 'fundamental'])
plt.title('Desempenho acadêmico nas escolas privadas vs públicas na educação fundamental')
plt.show()

##############


fundamental_privadas = df[(df['ensino'] == 'medio') & (df['rede'] == 'privada')]
fundamental_publicas = df[(df['ensino'] == 'fundamental') & ((df['rede'] == 'municipal') | (df['rede'] == 'estadual'))]#


t_statistic, p_value = ttest_ind(fundamental_municipais['taxa_aprovacao'], fundamental_estaduais['taxa_aprovacao'])
print("\nQuestão 3:")
print(f"T-Statistic: {t_statistic}")
print(f"P-Value: {p_value}")

sns.boxplot(x='rede', y='taxa_aprovacao', data=df[df['ensino'] == 'fundamental'])
plt.title('Taxa de aprovação nas escolas municipais vs estaduais na educação fundamental')
plt.show()


t_statistic, p_value = ttest_ind(fundamental_privadas['taxa_aprovacao'], fundamental_publicas['taxa_aprovacao'])
print("\nQuestão 4:")
print(f"T-Statistic: {t_statistic}")
print(f"P-Value: {p_value}")

sns.boxplot(x='rede', y='taxa_aprovacao', data=df[df['ensino'] == 'fundamental'])
plt.title('Taxa de aprovação nas escolas privadas vs publicas na educação fundamental')
plt.show()
