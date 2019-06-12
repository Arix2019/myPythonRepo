# tuplas - exibir os 5 primeiros numeros - os ultimos 4 numeros - colocar em ordem alfabetica - em qual posição esta o numero 17-

numeros = ('ZERO','UM','DOIS','TRÊS','QUATRO','CINCO','SEIS','SETE','OITO','NOVE','DEZ',
           'ONZE','DOZE','TREZE','QUATORZE','QUINZE','DEZESSEIS','DEZESSETE','DEZOITO',
           'DEZENOVE','VINTE')

print('='*50)
print('--> Os cinco primeiros números:', numeros[:6])
print('-'*50)
print('--> Os ultimos quatro números:', numeros[17:])
print('-'*50)
print('Ordem Alfabetica:', sorted(numeros))
print('-'*50)
print(f'--> O numero (17) está na {numeros.index("DEZESSETE")}º posição:')