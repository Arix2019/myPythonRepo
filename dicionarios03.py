'''
dicionarios 03
sintaxe de importação:  from bs4 import BeautifulSoup
'''



contato = {'nome':'Arix Batistix','data nascimento':'20121480','endereço':'rua zé ruela',
           'telefone':'56655525','email':'email@contato.com'}

contato2 = contato.copy()    # faz uma copia de 'contato' para 'contato2'

contato2['whatsapp'] = [96556838]   # adiciona em 'contato2'

for x in contato2.items():
    print(x)

contato2.pop('whatsapp')    # deleta um item da dicionario
# contato2.popitem()  # remove o primeiro item do dicionario

print('-'*30)
contato2.setdefault('Bairro','dead end')    # adiciona em 'contato2'

for x in contato2.items():
    print(x)

print(contato2.get('nome'))