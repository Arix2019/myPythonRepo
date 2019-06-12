'''
dicionarios 02
Métodos items, keys, values
Escreva tres funções(todas recebendo um dicionário)
items: Imprime uma lista de tuplas, sendo que cada tupla contenha a chave e o valor da
chave para dicionário.
Keys: Imprime uma lista contendo todas as chaves do dicinário
Values: Imprime uma lista contendo todos os valores da chave dicionário
'''

contato = {'nome':'Arix Batistix','data nascimento':'20121480','endereço':'rua zé ruela',
           'telefone':'56655525','email':'email@contato.com'}

'''
def dados(info,key,result=0):

    if key in info:
        print(key.upper(),':','',info[key].upper())
    else:
        print(f'Chave não encontrada: "{key}"')
    return False


chave = input('Chave de busca: ').lower()

dados(contato, chave)
'''


def items(dic):

    lista = []
    for key in dic:
        lista.append((key, dic[key]))
    print(lista)


def keys(dic):

    lista = []
    for key in dic:
        lista.append((key, dic[key]))
    print(lista)


def values(dic):

    lista = []
    for key in dic:
        lista.append((key, dic[key]))
    print(lista)


for i in contato.items():
    print(i)

print('-'*25)

for k in contato.keys():
    print(k)

print('-'*25)

for v in contato.values():
    print(v)