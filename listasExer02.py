
'''
programa onde o usuário possa digitar varios valores
neméricos e cadastre-os em uma lista. Caso o número ja
exista, ele nao será adicionado. No final serão exibidos
todos os valores unicos digitados, em ordem crescente.
'''
valores = []
testeValor = []
total = []
contagem = []
lista = [3, 0, 0, 0, 1, 1, 1, 0, 3, 3, 3]
#for x in set(lista):
    #print(lista.count(x),end='')
#    print(x)
for ocorrencia in lista:
    if total.count(ocorrencia) == 0:
        total.append(ocorrencia)
        contagem.append(lista.count(ocorrencia))
print(total)
print(contagem)