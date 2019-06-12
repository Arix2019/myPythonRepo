'''
programa que vai ler varios numeros e colocar em uma lista. Depois disso, crie duas
listas que vão conter os numeros pares e impares informados respectivamente.
Ao final mostre o conteudo das tres listas geradas.
'''
listNum = list()
listPar = list()
listImpar = list()

while True:
    num = int(input('>Informe um Número: '))
    listNum.append(num)
    resp = ' '
    while resp not in 'SN':
        resp = input('>>>Continuar? [S/N] ').upper().strip()[0]
    if resp == 'N':
        break

print('-+'*30)

qtd = len(listNum)

if qtd % 2 == 0:
    print(f'#Lista PAR com {qtd} elementos.')
else:
    print(f'#Lista IMPAR com {qtd} elementos.')

print(f'#Lista completa:  {listNum}')

for x in listNum:
    if x % 2 == 0:
        listPar.append(x)
    else:
        listImpar.append(x)

print(f'#Números pares contidos na lista:   {listPar}')
print(f'#Números Impares contidos na lista: {listImpar}')