# numeros primitivos:

# n1 = input('Numero: ')
# print(type(n1))
# resultado: <class 'str'>

# n2 = int(input('Numero: '))
# print(type(n2))
# resultado: <class 'int'>

# -----------------------------------------------

#n1 = bool(input('Numero: '))
#if n1 == True:
# print('OK! ',n1)
#else:
# print('ERRO! Digite algum numero.')

# -----------------------------------------------

# ordem de precedencia:
# 1 - ()
# 2 - **
# 3 - * / // %
# 4 - + -

# var.isnumeric( apenas numeros ) - var.isalpha( apenas letras ) - var.isalphanumeric( letras e numeros )
titu = 'Python'
print('='*20)
print('{:=^20}'.format(titu))

n1 = input('Digite: ')

if n1.isnumeric() == True:
 print('OK! Convertendo String para Inteiro -> ', n1, '+ 5 = ', int(n1) + 5)
else:
 print('ERRO! Informe apenas numeros.')