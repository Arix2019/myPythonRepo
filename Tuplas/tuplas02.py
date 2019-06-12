# tuplas

numeros = ('ZERO','UM','DOIS','TRÊS','QUATRO','CINCO','SEIS','SETE','OITO','NOVE','DEZ',
           'ONZE','DOZE','TREZE','QUATORZE','QUINZE','DEZESSEIS','DEZESSETE','DEZOITO',
           'DEZENOVE','VINTE')

while True:
    num = int(input('Informe o número: '))
    if num < 0 or num > 20:
        resp = ' '
        while resp not in 'SN':
            resp = input('Número não encontrado:[0 à 20] - Deseja Sair? {S/N}: ').strip()[0].upper()
        if resp == 'S':
           break
    else:
        print(f'Você digitou o número: {numeros[num]}')
        sair = ' '
        while sair not in 'SN':
            sair = input('Continuar? {S/N}: ').strip()[0].upper()
        if sair == 'N':
            break

