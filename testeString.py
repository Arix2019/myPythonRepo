#
#
#
texto = '''1681 <a href="javascript:carrega_concurso(1680);" tabindex=27><img
src="/loterias/_images/button/btn_conc_ant_lotofacil.jpg" alt="Ver
concurso anterior" border="0"></a>||01|02|03|07|08|10|11|12|15|16|17|20|22|23|25|8|178.602,81|533|1.178,33|14.709|20,00|158.950
8,00|828.206|4,00|<div id="titulo_ganhadores"><img src="/loterias/_images/title/ganhadores_estado_lotofacil.jpg"
title="Ganhadores por estado"></div><div id="ganhadores_novo_modelo">
<table><thead><tr><th class="largura_uf">UF</th><th>Nº de Ganhadores</th></tr></thead><tbody>
'''
'''
find_1 = '<img src="/loterias/_images/'
find_2 = '/ganhadores'
pos_1 = int(texto.index(find_1) + len(find_2))  # posicao 336
pos_2 = int(texto.index(find_2))    # posicao 358
resultado = texto[pos_1 + 17: pos_2]
print(resultado)
'''

print(f'{"Trecho:":.<20}',end='')
print(f'{texto[0:4]}')

