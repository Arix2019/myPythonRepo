'''
http://www1.caixa.gov.br/loterias/loterias/lotofacil/lotofacil_pesquisa_new.asp
Obtem dados da web
<img src="/dolar_hoje/img/icon-moeda-2.png" alt="Dólar Comercial" title="Dólar Comercial">
<input type="text" value="3,81" class="text-verde" id="comercial" calc="sim">
https://www.melhorcambio.com/dolar-hoje
'''
import urllib.request

url = urllib.request.urlopen('https://www.melhorcambio.com/dolar-hoje').read()
url = str(url)
busca = '<input type="text" value="'
pos = int(url.index(busca) + len(busca) + 1022)
dolar = url[pos:pos + 4]
print('-+'*30)
print(f'Dolar hoje: R${dolar}')