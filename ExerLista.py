'''
programa onde o usuário possa digitar varios valores neméricos e cadastre-os em uma lista.
Caso o número ja exista, ele nao será adicionado.
No final serão exibidos todos os valores unicos digitados, em ordem crescente.
'''
cadNum = []
num = 0
while num > -1:
    print('***(-1) para sair.***')
    print('-' * 25)
    num = int(input('> Cadastre um número: '))
    if cadNum.count(num) == 0:
        #print('>>Número adicionado com sucesso!')
        cadNum.append(num)
        #print(f'Elementos da Lista: {cadNum}')
    else:
        print('-'*25)
        print(f'>>>>AVISO! O número {num} já existe na lista.\n>> O elemento não foi adicionado.'.upper())
        #print(f'Elementos da Lista: {cadNum}')

for x in cadNum:
    if x < 0:
        cadNum.pop()

print('=' * 35)
print('\n>>>Lista Final:',sorted(cadNum))