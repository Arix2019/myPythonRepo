'''
gerar cinco numeros aleatorios e colocar em uma tupla - listar os numeros gerados -
indique o menor e maior valor que estao na tupla.
'''
from random import randint

aleatorios = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10),)
print(f'->O maior numero da lista {aleatorios} -> Foi o número {max(aleatorios)}\n->E '
      f'o menor foi o número {min(aleatorios)}')
