#GerarDados

import numpy as np
import pandas as pd
# Gerar dados simulados para diferentes contextos de engenharia com mais de 20 elementos

# Tempo em segundos
t = np.linspace(0, 10, 25)

# Engenharia Mecânica: Velocidade de um motor em função do tempo com ruído
velocidade = 2.5 * t**2 - 1.2 * t + 5 + np.random.normal(0, 2, t.shape)

# Engenharia Elétrica: Corrente em um circuito RC carregando
corrente = 10 * (1 - np.exp(-t / 2)) + np.random.normal(0, 0.5, t.shape)

# Engenharia Química: Concentração de um reagente ao longo do tempo em uma reação
concentracao = 100 * np.exp(-0.3 * t) + np.random.normal(0, 2, t.shape)

# Engenharia Civil: Deformação de uma viga sob carga ao longo do tempo
deformacao = 0.05 * t**3 - 0.4 * t**2 + 1.5 * t + 0.2 + np.random.normal(0, 0.2, t.shape)

# Convertendo os dados em lista e concatenando num dicionário
dados={
"tempo": t.tolist(),
"velocidade": velocidade.tolist(),
"corrente": corrente.tolist(),
"concentracao": concentracao.tolist(),
"deformacao": deformacao.tolist()}

#%%  Exportando para DataFrame
df=pd.DataFrame()
for i in dados.keys():
    df[i]=(dados[i])
df.to_csv('dados_eng.csv',index=False)    
#%% Exportando do DataFrame e escolhendo colunas para vetores
ndf=pd.read_csv('dados_eng.csv')
x=ndf[ndf.columns[0]].values
y=ndf[ndf.columns[1]].tolist()

'''
Para carregar apenas os valores use:
    * ".values" mantendo em array ou 
    * ".tolist()", trabalhando com lista

'''
#%% Gráficos
import matplotlib.pyplot as plt
for i in range(1,5):
    y=ndf[ndf.columns[i]].tolist()
    plt.figure()
    plt.title(f"Tempo x {ndf.columns[i]}") 
    plt.grid(True)
    plt.plot(x,y,'--',marker='o',markercolor='r')

    