"""programa que lê o ano de nascimento de sete pessoas.
No final mostre quantas pessoas ainda nao atingiram a
maior idade e quantas ja sao maiores.
EXercicio 54
"""

import datetime
totMaior = 0
totMenor = 0
for pessoa in range(1,6):
    dt_nasc = int(input('Em que ano a pessoa nasceu? '))
    idade = datetime.date.today().year - dt_nasc
    if idade >= 18:
        totMaior += 1
    else:
        totMenor += 1
print('Ao todo foram {} pessoas maiores de idade'.format(totMaior))
print('E {} pessoas menores de idade.'.format(totMenor))
