'''
'http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaCepEndereco.cfm'
sistemas/buscacep/resultadoBuscaCepEndereco.cfm
'''

from urllib.parse import urlencode
from urllib.request import Request, urlopen

def semEspacoXml(s):
    s = s.replace('&lt', '<')
    s = s.replace('&gt', '>')
    s = s.replace('&amp', '&')
    s = s.replace('&nbsp', ' ')
    return s

def semCaracteresEsp(s):
    s = s.replace('\\r', '')
    s = s.replace('\\t', '')
    s = s.replace('\\n', '')
    return s

def mostraCEP(dic,chave):
    if chave in dic:
        return dic[chave]
    else:
        return False

url = 'http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaCepEndereco.cfm'
postFields = {'relaxation': '70040010', 'tipoCEP': 'ALL', 'semelhante': 'N'}
request = Request(url, urlencode(postFields).encode())
result = urlopen(request).read()
result = str(result)

#   retira caracteres 'estranhos' e corrige acentuação:
result = semCaracteresEsp(result)
result = bytes(result, 'iso-8859-1').decode('unicode_escape')
result = semEspacoXml(result)

#   busca a primeira posição requisitada e 'limpa' o código
busca = 'CEP:</th>'
pos = int(result.index(busca) + len(busca))
result = result[pos: pos + 200]

#   separa a Rua
buscaInicio = '<td width="150">'
buscaFinal = ';</td><td width='
posInicio = int(result.index(buscaInicio) + len(buscaFinal))
posFinal = int(result.index(buscaFinal))
resultRua = result[posInicio: posFinal]

#   separa o Bairro
buscaInicio = '<td width="90">'
buscaFinal = '<td width="80">'
posInicio = int(result.index(buscaInicio) + len(buscaFinal))
posFinal = int(result.index(buscaFinal))
resultBairro = result[posInicio: posFinal - 6]

#   separa a Cidade
buscaInicio = '<td width="80">'
buscaFinal = '<td width="55">'
posInicio = int(result.index(buscaInicio) + len(buscaFinal))
posFinal = int(result.index(buscaFinal))
resultCidade = result[posInicio: posFinal - 5]

#   resultado da busca por CEP:
print('-+'*25)
print('Informações sobre o CEP:', mostraCEP(postFields,'relaxation'))
print('Logradouro:', resultRua)
print('Bairro:', resultBairro)
print('Cidade/Estado:', resultCidade)