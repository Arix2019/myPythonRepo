'''
percorrer uma matriz e imprimi-la de forma tabular:
'''

matriz = [[1,2,3], [4,5,6], [7,8,9]]
'''
for x in matriz:
    for y in x:
        print(y, end=' ')
    print('\n')
'''
for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        if l == c:
            print('X', end=' ')
        else:
            print('O',end=' ')
    print('\n')