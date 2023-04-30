simbolo = linha[0]
empresa = linha[1]
tipo_acao = linha[2]
composicao = linha[3]
perc_payout_estatuto = linha[4]
dy_med_trien = linha[5]
preco_atual = linha[6]
qtd_meta = linha[7]
qtd_autal = linha[8]
vl_investido = linha[9]
previsao_receber = linha[10]
patri_liq_antes = linha[11]
lucro_liq_antes = linha[12]
acoes_emitididas = linha[13]

Variavel 1 = 0,08
-----------------------------------------------------

Preco Teto
===== ====
(10) / Variavel 1


-----------------------------------------------------
(3) Preço / Yield
=== ===== = =====
(10)/(11) -> DY MÉDIO, dividido por PREÇO ATUAL
Em precentual
linha[5] / linha[6]


(10) DY MÉDIO 3 a.a -> 2,26
(11)PREÇO ATUAL Mercado
-----------------------------------------------------
(5) Gatilho 3/8
=== ======= ===
se (11) <= (12) => "comprar" se não "não compra"


(6) Gatilho 3/8 ajustado
=== ======= === ========
se (11) <= (13) => "comprar" se não "não compra"

