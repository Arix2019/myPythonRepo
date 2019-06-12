#
lista = [5,15,45,85,5,25,33,66,77,85,85,5,1,10,12,12,37,37,82,85,85,10]
total = []
total2 = []
repetidos = []

for contagem in lista:
    if total.count(contagem) == 0:
        total.append(contagem)
    else:
        total2.append(contagem)

    if lista.count(contagem) == 1:
        repetidos.append('X')
    else:
        repetidos.append(lista.count(contagem))

print('Lista sem repetições:        ',total)
print('Números de repetições:       ',repetidos)
print('Apenas os números repetidos: ',total2)
print('-'*100)
print('Combinação: ')
print('Lista Completa:\n',lista)
print('Número de repetições:\n',repetidos)
print(f'São {len(lista)} elementos na lista original e {len(repetidos)} na lista de repetições. O (0) '
      f'corresponde ao número equivalente que não se repete.')
