# manipulação de textos 2

frase = '  ignorance is bliss  '
print('==== Manipulação de Textos ====')
print('-> Substituindo trecho da frase: "{}" por "{}" '.format(frase,frase.replace('ignorance','igNoRaNcE')))
print('-> Transforma todas as letras em maiusculas: ',frase.upper())
print('-> Transforma todas as letras em minusculas: ',frase.lower())
print('-> Deixa apenas a primeira letra em maiuscula: ',frase.capitalize())
print('-> Letra maiuscula em cada inicio de palavra: ',frase.title())
print('-> A frase: "{}" continha {} caracteres (contando espaços). '.format(frase,len(frase)))
nova = frase.strip()
print('-> Agora a frase "{}" contém {} caracteres eliminando os espaços anterios e posteriores a ela. '.format(frase.strip(),len(nova)))
print('-> Eliminado espaços a direita da frase:',frase.rstrip())
print('-> Eliminado espaços a esquerda da frase:',frase.lstrip())
print('-> Separa a frase em palavras: ',frase.split())
print('-> Insere o caracter (-) entre as letras da frase: ','-'.join(nova))
print(f'-> A lentra (n) esta na {frase.strip().index("n")+1}º posição da frase {frase.strip().upper()}.'
      f' Ao todo são {frase.count("n")} letras (n).')