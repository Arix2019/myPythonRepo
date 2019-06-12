'''
programa onde usuario digita uma expressão qualquer que use parenteses. Seu
aplicativo deverá analisar se a expressão passada esta com os parenteses abertos e
fechados na ordem correta.

OUTRA FORMA:

contExp01 = 0
contExp02 = 0

exp = input('>Digite a expressão: ')     #   list(input('Digite a expressão: '))
for x in range(len(exp)):
    if exp[x] == '(':
        contExp01 += 1
    elif exp[x] == ')':
        contExp02 += 1
if contExp01 == contExp02:
    print('>>Expressão válida!')
else:
    print('>>Expressão inválida!')
'''

exp = input('>>Digite a expresão: ')

print('-+'*20)
if exp.count('(') == 0:
    print('>>>Não parece uma expressão comum. ')

elif exp.count(')') == 0:
    print('>>>Não parece uma expressão comum. ')

elif exp.count('(') == exp.count(')'):
    print('>>>Expressão Válida!')

else:
    print('>>>ERRO!\nFaltaram parâmetros para sua expressão!')

