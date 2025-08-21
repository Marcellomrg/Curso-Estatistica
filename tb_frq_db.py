# %%
import pandas as pd
import sqlalchemy

df = pd.read_csv("data/dados_origem.csv")
df.head()
# %%
engine = sqlalchemy.create_engine("sqlite:///data/tw.db")
df.to_sql("points",if_exists="replace",index=False,con=engine)
# %%

# %%
