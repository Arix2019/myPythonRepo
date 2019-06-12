# testes listas Python
'''
num = [8,9,4,7,3,12]

num.append(14) #adiciona o elemento 14 no final da lista
#num.sort() #num.sort(reverse=True)
num.insert(1,18) # adiciona o elemento (18) na sugunda posição da lista contando do 0...
#num.pop(1) #deleta o segundo item da lista - pop() -> apaga o ultimo item da lista.
if 3 in num:
    num.remove(3)
else:
    print('Item não existe na lista.')
print(f'A lista {num} tem {len(num)} elementos.')
'''
valores = list() #ou []
valores.append(5)
valores.append(9)
valores.append(7)

#for v in valores:
#    print(f'...{v}', end=' ')
for c,v in enumerate(valores): #enumerate encontra o indice de cada item
    print(f'Na posição {c} encontrei o valor {v}!')
print('FIM!')