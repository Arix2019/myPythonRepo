# testes laço while 2 - media entre numeros

sair = ''
media = 0
somaNumeros = 0
cont = 0
while sair != 'S':
    num = int(input('Numero: '))
    cont = cont + 1 # conta a quantidade de numero informados
    somaNumeros += num #   soma os numeros digitados
    sair = input('\tSair? [S/N]: ').upper()

media = somaNumeros / cont
print(f'Foram informados {cont} números,a soma de todos foi: {somaNumeros} e a média: {media} ')