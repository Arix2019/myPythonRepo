'''
dicionario 01
'''

contato = {'Nome:':'Arix Batistix','Endereço:':'R. Ze Ruela',
           'Telefone:':56655525,'E-Mail:':'email@contato.com'}


def getDados(info,chave,valor=0):

    if chave in info:
        return info[chave]
    else:
        return valor


print(getDados(contato,'Nome:'))
print(getDados(contato,'E-Mail:'))
print(contato.get('Endereço:'),'',contato.get('Telefone:'),'',contato.get('E-Mail:'))