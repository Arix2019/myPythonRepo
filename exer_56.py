"""
EXEMPLO 56-
programa que lê o nome,idade e sexo de 4 pessoas.
no final mostre:
- a media de idade.
- nome do homem mais velho
- quantas mulheres tem menos de 20 anos
"""
somaIdade = 0
mediaIdade = 0
maiorIdHomem = 0
nomeHmaisVelho = ''
totMulherMenor20 = 0
for p in range(1,5):
    print('----{}º Pessoa:----'.format(p))
    nome = input('Nome: '.strip())
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: '.strip())
    somaIdade += idade
    if p == 1 and sexo.upper() == 'M':
        maiorIdHomem = idade
        nomeHmaisVelho = nome
    if sexo.upper() == 'M' and idade > maiorIdHomem:
        maiorIdHomem = idade
        nomeHmaisVelho = nome.upper()
    if sexo.upper() == 'F' and idade < 20:
        totMulherMenor20 += 1
mediaIdade = somaIdade / 4
print('A média de idade do grupo é de: {} anos.'.format(mediaIdade))
print('{} é o homem mais velho com {} anos.'.format(nomeHmaisVelho.upper(),maiorIdHomem))
print('{} mulher(es) menor(es) de 20 anos.'.format(totMulherMenor20))
