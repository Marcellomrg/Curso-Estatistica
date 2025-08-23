-- Estatisticas dados usuarios-----
WITH tb_usuario as
( SELECT idUsuario,sum(qtdPontos) as qtdPontos 
from points GROUP BY idUsuario),


minimo as (
            SELECT min(qtdPontos) as minimo from tb_usuario),

tb_quartile1 as (SELECT qtdPontos as quartile1 from 
(SELECT * from tb_usuario  ORDER BY qtdPontos LIMIT 1 
OFFSET (SELECT 1 * count(*) / 4 FROM tb_usuario))),

mediana as (SELECT AVG(qtdPontos)as mediana FROM 
(SELECT * FROM tb_usuario ORDER BY qtdPontos LIMIT 1 + 
(SELECT count(*)%2==0 FROM tb_usuario)
OFFSET (SELECT count(*) / 2 from tb_usuario))),

tb_quartile3 as (SELECT qtdPontos  as quartile3 
from (SELECT * FROM tb_usuario 
ORDER BY qtdPontos LIMIT 1
OFFSET (SELECT 3 * count(*) / 4  FROM tb_usuario))),

maximo as (SELECT max(qtdPontos) from tb_usuario),

media as (SELECT avg(qtdPontos) from tb_usuario)

SELECT * from minimo,tb_quartile1,
mediana,tb_quartile3,maximo,media





