from bs4 import BeautifulSoup

htmlData = '''
    1680|<a href="javascript:carrega_concurso(1679);" tabindex=27>
    <img src="/loterias/_images/button/btn_conc_ant_lotofacil.jpg" alt="Ver concurso anterior" border="0">
    </a>||01|02|03|07|08|10|11|12|13|14|18|20|21|23|25|2|537.770,69|782|604,55|26.705|20,00|244.221|8,00|1.101.865|4,00|
    <div id="titulo_ganhadores"><img src="/loterias/_images/title/ganhadores_estado_lotofacil.jpg" title="Ganhadores por estado">
    </div><div id="ganhadores_novo_modelo">
    <table><thead><tr><th class="largura_uf">UF</th>
    <th>Nº de Ganhadores</th>
    </tr>
    </thead>
    <tbody><tr class="destaca_estado">
    <td>AL</td>
    <td>1</td>
    </tr>
    <tr><td><span>MACEIÓ</span></td><td>1</td>
    </tr><tr class="destaca_estado"><td>BA</td><td>1</td>
    </tr><tr><td><span>SALVADOR</span></td><td>1</td></tr>
    </tbody></table></div>|<span style="font-size: 14px; font-weight: bold;">Estimativa de Prêmio</span><br />
    <span style="color: rgb(102, 102, 102); font-size: 22px; font-weight:bold;">R$</span>
    <span style="font-size: 22px; color:#911687; font-weight: bold;">1.700.000,00</span>
    <br /><span style="font-size: 13px;">*para o próximo concurso, a ser realizado em 27/06/2018</span>
    <br /><br />|<a class="btn_impressaoLoterias" href="javascript:imprimir_lotofacil(1680);"
    title="Imprimir resultado">Imprima o resultado</a>
    |SÃO PAULO|SP|ESPAÇO LOTERIAS CAIXA|25/06/2018
    ||0|0|20|13|23|18|25|10|08|02|01|21|12|07|14|03|11|1.700.000,00|27/06/2018|21.359.420,00|57.053.016,68
'''

soup = BeautifulSoup(htmlData, 'lxml')

print(soup.findAll('a'))