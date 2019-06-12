# teste laço While

'''n = 1
cont = 0
while n != 0:
    n = int(input('Valor: '))
    if n != 0:
        cont += 1
print('FIM!', cont)'''

# leia a idade e o sexo de pessoas: - qts pessoas com mais de 18 anos -
# qts homens foram cadastrados - qts mulheres tem menos de 20 anos
cont = 1
idade = 0
contFinal = 0
nome = ' '

while True:
    print(f'========={cont}ºPessoa=========')
    #nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo[M/F]: ').strip()[0].upper()

    resp = ' '
    while resp not in 'SN':
        resp = input('Continuar? [S/N]').strip()[0].upper()
        cont += 1
        contFinal = cont - 1
    if resp == 'N':
        break
print(f'\n*** Foram cadastradas {contFinal} pessoas. ***')
print('='*30)