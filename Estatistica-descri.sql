-- Estatistica descritivas da coluna Qnt de pontos
with minimo as (
                SELECT min(qtdPontos) as minimo from points),

tb_quartile1 as (SELECT qtdPontos as quartile1 from 
(SELECT * from points  ORDER BY qtdPontos LIMIT 1 
OFFSET (SELECT count(*)*0.25 FROM points))),

mediana as (SELECT AVG(qtdPontos)as mediana FROM 
(SELECT * FROM points ORDER BY qtdPontos LIMIT 1 + 
(SELECT count(*)%2==0 FROM points)
OFFSET (SELECT count(*) /2 from points))),

tb_quartile3 as (SELECT qtdPontos  as quartile3 
from (SELECT * FROM points 
ORDER BY qtdPontos LIMIT 1
OFFSET (SELECT count(*) * 0.75  FROM points))),

maximo as (SELECT max(qtdPontos) from points),

media as (SELECT avg(qtdPontos) from points)

SELECT * from minimo,tb_quartile1,
mediana,tb_quartile3,maximo,media

