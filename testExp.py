#parte do arquivo funcExp.py
from funcExp import exp

string = input('>>>Digite a expressão: ')

print('-+'*20)
if exp(string) == 0:
    print('>>>Parâmetros aceitos.')
else:
    print('>>>A sintaxe da sua expressão possui erros.')



