# Laço FOR parte2

""""# exibe numeros pares de 0 a 5:
for cont in range(0,6,2):
    print(cont)"""

"""num = int(input('Numero: '))
for cont in range(1,11):
    print('{} x {:2} = {}'.format(num,cont,num * cont))
print('='*12)"""

"""inicio = int(input('Número inicial: '))
maximo = int(input('Número Máximo: '))
salto = int(input('Saltando: '))
for cont in range(inicio,maximo+1,salto):
    print(cont)
print('fim!')"""

listPar = par = 0
listImpar = impar = 0
for cont in range(1,6):
    n = int(input('Número: '))
    if n % 2 == 0:
        par += 1
        #for listPar in range(par):
        #    print(listPar)
    else:
        impar += 1
        #for listImpar in range(impar):
        #    print(listImpar)

print('Foram digitados {} números pares e {} números impares.'.format(par,impar))
