WITH tb_frq_abs AS
(SELECT descProduto,count(idTransacao) AS Freq_abs 
FROM points 
GROUP BY descProduto),

tb_frq_abs_cum AS (
    SELECT *,
            sum(Freq_abs) OVER (ORDER BY descProduto) as FreqAbsAcum,

            1.0 *Freq_abs / (SELECT sum(Freq_abs) FROM tb_frq_abs) AS FreqRelativa
    from  tb_frq_abs

) 

SELECT * ,sum(FreqRelativa) OVER (ORDER BY descProduto) as FreqRelativaAcum


FROM tb_frq_abs_cum