import numpy as np
import pandas as pd
from math import ceil

populacao = 150
amostra = 15
k = ceil(populacao / amostra)

r = np.random.randint(low = 1, high = k + 1, size = 1 )
# parte 'r' é um sorteio entre os 10 classificados
acumulador = r[0]
sorteados = []
for i in range(amostra):
    #pirint (acumulador)
    sorteados.append(acumulador)
    acumulador += k # o acumulardor mais o numero K, gerando uma amostra de 10 a 10
    
base =  pd.read_csv('iris.csv')
base_final = base.loc[sorteados] 
# base.loc é uma forma de localizar as flores segundo as mostras sorteadas 