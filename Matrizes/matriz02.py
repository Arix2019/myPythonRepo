#matriz
matriz = [[1,2,3],[4,5,6],[7,8,9]]

for x in matriz:
    print(x,end='')
    print('\n')

# -------------
matriz[0][0] = 'X'
matriz[1][1] = 'X'
matriz[2][2] = 'X'
matriz[0][1] = 0
matriz[0][2] = 0
matriz[1][0] = 0
matriz[1][2] = 0
matriz[2][0] = 0
matriz[2][1] = 0

print('-'*20)
for y in range(len(matriz)):
    for z in range(len(matriz[y])):
        print(matriz[y][z], end=' ')
    print('\n')