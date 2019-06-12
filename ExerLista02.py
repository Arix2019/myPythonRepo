'''
programa que vai ler varios números e colocar em uma lista. Depois disso mostre:
a) Qts números foram digitados
b) A lista de valores ordenadas de forma decrescente
c) Se o valor 5 for digitado e esta ou não na lista.
'''

numDigitados = list()
reverseNum = list()
num = 0
while num > -1:
    num = int(input('Digite um número: '))
    numDigitados.append(num)

numDigitados.pop() #retira o ultimo numero da lista
numDigitados.sort() #coloca a lista em ordem crescente

print(f'Foram informados {len(numDigitados)} elementos.')
print('>>>Lista em ordem decrescente: ',list(reversed(numDigitados))) #coloca em ordem decrescente

if 5 in numDigitados:
    print(f'>>>O número 5 esta na lista! >> '
          f'E está na {numDigitados.index(5)}º posição (decrescente).')
else:
    print('>>>O número 5 NÃO esta na lista.')

