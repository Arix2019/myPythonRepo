# numeros primitivos:

print('='*20)
n = input('Numero: ')
if n.isnumeric() == True:
 sucessor = int(n) + 1
 antecessor = int(n) - 1
 print('O Antecessor de {} é: {} \nO Sucessor de {} é: {}'.format(n,antecessor,n,sucessor))
else:
 print('ERRO! Informe apenas números.')