# %%
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import t as t_student
# %%
df = pd.read_csv("data/dados_origem.csv")
df.head()
# %%
usuarios = (df.groupby(by="idUsuario")["qtdPontos"]
            .sum()
            .reset_index())
usuarios.head()
# %%
# I.C = X_bar - t_student * sigma/sqrt(n)
n = 100
sample = usuarios["qtdPontos"].sample(n)


def intervalo(sample,alpha = 0.05):

    n = len(sample)
    x_bar = sample.mean()
    t = t_student.ppf(1-alpha/2,n-1)
    s = sample.std()

    intervalo_inferior = x_bar - t*s/(n**(0.5))

    intervalo_superior = x_bar + t*s/(n**(0.5))

    return x_bar,s,intervalo_inferior,intervalo_superior
# %%
intervalo(sample)
# %%
stats = []
for i in range(1000):
    n = 100
    sample = usuarios["qtdPontos"].sample(n)
    stats.append(intervalo(sample))


stats = pd.DataFrame(stats,columns=["media","Desvio","inf","sup"])

stats
# %%
stats["Verdadeiro"] = usuarios["qtdPontos"].mean()
stats
# %%
stats["check"] = (stats["Verdadeiro"]>stats["inf"]) & (stats["Verdadeiro"]<stats["sup"])
stats["check"].mean()
# %%
for i in range(30):
    data = stats.iloc[i]
    color = 'green' if data["check"] else "red"
    plt.plot(data[["inf","sup"]],[i,i],'o--',color=color,alpha = 0.5)

plt.vlines(data["Verdadeiro"].max(),-1,31,color='black',alpha=0.5)
plt.grid()
plt.show()
plt.savefig("Intervalo de Confiança")
# %%
