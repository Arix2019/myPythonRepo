
valores = []
x = 0
for cont in range(0,5):
    print(f'{x}º',end=' ')
    valores.append(int(input('Valor: ')))
    x += 1
for pos,v in enumerate(valores):
    if v == max(valores):
        print(f'O maior valor {max(valores)} está na posição {pos}.')
    elif v == min(valores):
        print(f'O menor valor {min(valores)} está na posição {pos}.')
print(f'Lista: {valores}')