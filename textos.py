# manipulação de textos

frase = 'Ignorance is Bliss'
#for x in range(len(frase)):
#    print(frase[x])
print('====Manipulação de textos====')
print('A frase: "{}" possui {} caracteres.'.format(frase,len(frase)))
print('Do 9º caracter ate o 18º: ',frase[9:18])
print('Do 9º caracter ate o ultimo: ',frase[9:len(frase)])
print('Exibe os 9 primeiros caracteres: ',frase[:9])
print('Exibe do 15º caractere ate o 18º: ',frase[14:])
print('Exibe do 9º caractere ate o 18º pulando 1 casa: ',frase[9:18:2])
print('A frase "{}" possui {} letras (s).'.format(frase,frase.count('s')))
print('A frase "{}" pussui {} letra (s) entre o 1º e o 12º caracter.'.format(frase,frase.count('s',0,12)))
print('O trecho (is) esta na posição {} (contando apartir do 0) da frase: "{}". '.format(frase.find('is'),frase))
print('Se o (find) nao encontrar o trecho procurado na frase ele retornará o erro: {}'.format(frase.find('MENOS 1')))

teste = 'Bliss' in frase
print('Existe a palavra (Bliss) na frase "{}"¿'.format(frase))
if teste == True:
    #print('Existe a palavra (Bliss) na frase "{}"¿ {}'.format(frase,teste))
    print('Resposta: Sim.')
else:
    print('Resposta: Não.')