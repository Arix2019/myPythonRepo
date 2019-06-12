#leia quatro valores e guarde-os em um tupla. no final mostre:
#qts vezes apareceu o valor 9 - em qual posição foi digitado o primeiro valor 3
#quais foram os numeros pares

valores = (int(input('1º Valor: ')),int(input('2º Valor: ')),int(input('3º Valor: ')),
           int(input('4º Valor: ')))

print(f'O numero (9) apareceu {valores.count(9)} vez(es) entre os números {valores}.')
if 3 in valores:
    print(f'O número (3) apareceu na {valores.index(3)+1}º posição.')
else:
    print('Não foi encontrado o numero 3.')
print('Numeros pares: ',end='')
for n in valores:
    if n % 2 == 0:
        print(n, end=' ')