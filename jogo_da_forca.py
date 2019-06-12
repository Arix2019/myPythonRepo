# jogo da forca - PYTHON

palavraChave = ['S','M','I','L','E']
letraChave = []

print('\n*** Jogo da Forca ***')

for x in range(0,len(palavraChave)):
    letraChave.append('-')
acertou = False

while acertou == False:
    letra = input('>>Digite uma Letra: ').strip()[0].upper()
    for i in range(0,len(palavraChave)):
        if letra == palavraChave[i]:
            letraChave[i] = letra
        print(letraChave[i],end='  ')
    acertou = True

    for y in range(0,len(letraChave)):
        if letraChave[y] == '-':
            acertou = False
print('\nParabens! Você venceu.')