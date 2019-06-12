# laço for exercicios

"""
programa que leia uma frase qualquer e diga se ela é um palindromo
ex: APOS A SOPA (DE TRAS PRA FRENTE É A MESMA FRASE)
"""

frase = 'Apos a Sopa'
frase2 = 'Testando'

result = ''
for r in reversed(frase):
    result = result + r
print(result.lower())

print(list(reversed(frase)))

# range
frase = range(1,8)
print(list(reversed(frase)))