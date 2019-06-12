'''
executavel no arquivo (testExp.py)
função teste
'''

def exp(strExp):

    contExp01 = contExp02 = 0

    for i in range(len(strExp)):
        if strExp[i] == '(':
            contExp01 += 1
        elif strExp[i] == ')':
            contExp02 += 1

    if contExp01 == contExp02:
        return 0
    else:
        return 1

'''
string = input('>>>Digite a expressão: ')

print('-+'*20)
if exp(string) == 0:
    print('>>>Parâmetros aceitos.')
else:
    print('>>>A sintaxe da sua expressão possui erros.')
'''