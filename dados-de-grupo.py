# leia a idade e o sexo de pessoas: - qts pessoas com mais de 18 anos -
# qts homens foram cadastrados - qts mulheres tem menos de 20 anos
cont = 1
idade = 0
contIdade = 0
contH = 0
contM = 0
contMmenor = 0
contPessoas = 0
nome = ' '

while True:
    print(f'========={cont}ºPessoa=========')
    idade = int(input('Idade: '))
    if idade > 18:
        contIdade += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo[M/F]: ').strip()[0].upper()
        if sexo == 'M':
            contH += 1
        else:
            contM += 1
            if contM < 20:
                contMmenor += 1
    resp = ' '
    while resp not in 'SN':
        resp = input('Continuar? [S/N]').strip()[0].upper()
        cont += 1 #conta o numero de cadastros
        contPessoas = cont - 1
    if resp == 'N':
        break

print(f'\n***Informações***\n{contPessoas} Pessoa(s) cadastrada(s).\n{contIdade} Pessoa(s) maior(es) de 18 ano(s).\n{contH} Homen(s).')
print(f'{contMmenor - 1} melher(es) com menos de 20 ano(s).')
print('='*30)