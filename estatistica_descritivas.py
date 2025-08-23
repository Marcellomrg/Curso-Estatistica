# %%
import pandas as pd

# %%
df = pd.read_csv("data/dados_origem.csv")
df.head()

# %%
# Minimo qnt de pontos
minimo = df["qtdPontos"].min()
minimo
# %%
# Primeiro Quartil -Qnt pontos
quartil1 = df["qtdPontos"].quantile(0.25)
quartil1
# %%
# Mediana -Qnt pontos
mediana = df["qtdPontos"].quantile(0.5)
mediana
# %%
# Quartile 3 -Qnt pontos
quartil3 = df["qtdPontos"].quantile(0.75)
quartil3
# %%
maximo = df["qtdPontos"].max()
maximo
# %%
media = df["qtdPontos"].mean()
media
# %%
variancia = df["qtdPontos"].var()
variancia
# %%
desvio_padrao = df["qtdPontos"].std()
desvio_padrao
# %%
amplitude = df["qtdPontos"].max() - df["qtdPontos"].min()
amplitude
# %%
# Estatisticas descritivas do total de pontos 
# e qnt de transacoes por usuario
Summary = (df.groupby(by="idUsuario").
           agg({"qtdPontos":"sum","idTransacao":"count"})
           .rename(columns={"qtdPontos":"TotalPontos","idTransacao":"QntTransacoes"}))
Summary.head()
# %%
Estatistica_descritivas = Summary[["TotalPontos","QntTransacoes"]].describe()
Estatistica_descritivas

# %%
