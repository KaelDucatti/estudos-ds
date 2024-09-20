import pandas as pd

df = pd.read_csv("imigrantes_canada.csv")

df


df.columns
for i in range(10):
    if i % 2 == 0:
        print(i)


df["1980"].sum()

# Para executar código no Terminal Jupyter
# Executar uma linha: shift + enter
# Executar a linha atual e todas as linhalinhas abaixo: ctrl + shift + b
# Executar o módulo inteiro: ctrl + alt + j