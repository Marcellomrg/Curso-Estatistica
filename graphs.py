# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/dados_origem.csv")
df.head()
# %%
transacoes_produto = (df.groupby(by="descProduto")["idTransacao"]
                        .count()
                        .reset_index())
transacoes_produto = transacoes_produto.sort_values(by="idTransacao")
# %%
# Grafico barra
plt.bar(transacoes_produto["descProduto"],transacoes_produto["idTransacao"])
plt.show()
# %%
plt.figure(figsize=(6,4))
sns.barplot(transacoes_produto,x="idTransacao",y="descProduto")
plt.xlabel("Quantidade de transacoes")
plt.ylabel("Produto")
plt.title("Frequencia de produtos")
plt.savefig("Grafico de barras do produto")
plt.show()
# %%
# Grafico linhas 

df["dtTransacao"] = pd.to_datetime(df["dtTransacao"]).dt.date
df
# %%
transacao_diaria = (df.groupby(by="dtTransacao")
                    .agg({"qtdPontos":"sum","idTransacao":"count"})
                    .reset_index()
                    )
transacao_diaria = transacao_diaria.sort_values(by="dtTransacao")
transacao_diaria

# %%
plt.figure(figsize=(8,6))
plt.plot(transacao_diaria["dtTransacao"],transacao_diaria["idTransacao"])
plt.title("Serie historica de transacoes")
plt.ylabel("Qnt. de transacoes")
plt.legend("Qnt. de transacoes")
plt.show()
plt.savefig("Grafico serie historica de transacoes")
# %%
# Grafico histograma

plt.hist(transacao_diaria["qtdPontos"],bins=18,density=True)
plt.xlabel("Pontos")
plt.savefig("Grafico de pontos")
plt.show()
# %%
# Grafico bloxplot
plt.boxplot(transacao_diaria["qtdPontos"])
plt.ylabel("Pontos")
plt.title("Box-plot")
plt.savefig("Grafico blox-plot")
plt.show()
# %%
#Grafico Dispersao

sns.scatterplot(transacao_diaria,x="qtdPontos",y="idTransacao")
plt.ylabel("Qnt de transacoes")
plt.title("Grafico dispersao")
plt.savefig("Grafico de dispersao")
plt.show()
# %%
