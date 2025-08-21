# %%
import pandas as pd

# %%
df = pd.read_csv("data/dados_origem.csv")
df.head()
# %%
# Tabela Frequencia desc Produto
df_produto= (df.groupby(by="descProduto")[["idTransacao"]].count().
        rename(columns={"idTransacao":"Freq.Abs"}))
df_produto
# %%
df_produto["Freq.Abs Acum"] = df_produto["Freq.Abs"].cumsum()
df_produto
# %%
df_produto["Freq.Relativa"] = df_produto["Freq.Abs"]/df_produto["Freq.Abs"].sum()
df_produto
# %%
df_produto["Freq.Relativa ACum"] = df_produto["Freq.Relativa"].cumsum()
df_produto
# %%
# Tabela Frequencia categoria produto
df_categoria = (df.groupby(by="descCategoriaProduto")[["idTransacao"]].count()
                    .rename(columns={"idTransacao":"Freq.Abs"}))
df_categoria
# %%
df_categoria["Freq.Abs Acum"] = df_categoria["Freq.Abs"].cumsum()
df_categoria
# %%
df_categoria["Freq.Relativa"] = df_categoria["Freq.Abs"]/df_categoria["Freq.Abs"].sum()
df_categoria
# %%
df_categoria["Freq.Relativa Acum"] = df_categoria["Freq.Relativa"].cumsum()
df_categoria
# %%
