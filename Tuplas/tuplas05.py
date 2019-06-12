#   programa que tenha uma tupla com varias palavras
#   mostrar para cada palavra quais são suas vogais.

marcas = ('apple','motorola','sony','samsung','huawey','positivo','asus')

print(f'{"Lista do vogais":-^65}')
for m in marcas:
    print(f'\nNa marca {m.upper()} temos as seguintes vogais: ',end='')
    for letras in m:
        if letras in 'aeiou'.lower():
            print(list(letras),end='')