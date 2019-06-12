'''
RETORNA O RESULTADO MAIS RECENTE DA LOTOFÁCIL:
'''
import requests

url = 'http://www1.caixa.gov.br/loterias/loterias/lotofacil/lotofacil_pesquisa_new.asp'
req = requests.get(url)
req = req.text

#   busca numeros reultado
busca = '</a>||'
pos = int(req.index(busca) + len(busca))
result = req[pos: pos + 44]
resultSorteio = result.replace('|','-')

#   busca valor premiação
buscaPre = 'e: 22px; color:#911687; font-weight: bold;">'
buscaPreFinal = '</span><br /><span style="font-size: 13px;">'
posPre = int(req.index(buscaPre) + len(buscaPreFinal))
posFinal = int(req.index(buscaPreFinal))
resultPremio = req[posPre: posFinal]

print(f'{"Lotofácil":=^30}')
print(f'{"Concurso:":.<15}',req[0:4])
print(f'{"Resultado:":.<15}', resultSorteio)
print(f'{"Premiação:":.<15}','R$',resultPremio)