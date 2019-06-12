'''
programa onde o usuário possa digitar varios valores
neméricos e cadastre-os em uma lista. Caso o número ja
exista, ele nao será adicionado. No final serão exibidos
todos os valores unicos digitados, em ordem crescente.
'''
total = []
contagem = []
#lista = [5,4,6,8,5,6,15,25,35,78,25,25,4,10,12,13,10,13,66,99,98,66]
lista = [5,4,0,2,3,0,4,4]

for ocorrencia in lista:
    if total.count(ocorrencia) == 0:
        total.append(ocorrencia)   #'total.append' adiciona a quantidade de numeros q nao sao repetidos
        contagem.append(lista.count(ocorrencia))    #contagem.append adiciona

print('Lista original: ',lista)
print('Exclui os numeros repetidos: ',total)
print('Lista a quantidade de cada numero repetido: ',contagem)