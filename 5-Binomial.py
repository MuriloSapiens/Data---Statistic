from scipy.stats import binom

# Jogar uma moeda 5 vezes, qual a probabilidade de dar 3 vezes cara?
prob = binom.pmf(3, 5, 0.5) # X=3, n=5, p=0.5

#Passar por 4 sinais de 4 tempos, qual a probabilidade de pegar o sinal verde
# nehuma, 1, 2, 3, ou  4 vezes?
# x=0,1,2,3,4 n=4 p=0.25
prob2 = binom.pmf(0, 4, 0.25) ,binom.pmf(1, 4, 0.25), binom.pmf(2, 4, 0.25), binom.pmf(3, 4, 0.25), binom.pmf(4, 4, 0.25)

# E se forem sinais de dois tempos?
prob3 = binom.pmf(0, 4, 0.5) ,binom.pmf(1, 4, 0.5), binom.pmf(2, 4, 0.5), binom.pmf(3, 4, 0.5), binom.pmf(4, 4, 0.5)

#Probabilidade acumulativa
binom.cdf(4, 4, 0.25)

#Concurso com 12 questões, qual a probabilidade de acertar 
#7 questões considerando que cada questão tem 4 alternativas?
binom.pmf(7, 12, 0.25) * 100

binom.pmf(12, 12, 0.25) * 100