'''
utiliza uma API para fazer consulta por informações
sobre filmes na web.
'''
import requests
import json

req = None
try:
    req = requests.get('http://www.omdbapi.com/?i=tt3896198&apikey=79aeaaeb')
except:
    print('Falha de conexão.')
    exit()

#   print(req.text)

dic = json.loads(req.text)

print(dic)
print('-+'*25)
print('Título: ',dic['Title'])
print('Ano: ',dic['Year'])
print('Diretor: ',dic['Director'])
print('Atores: ',dic['Actors'])
print('Avaliação: ',dic['imdbRating'])