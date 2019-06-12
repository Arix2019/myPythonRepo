#
dadosPessoais = [['Dido',38,'cantora'],
                 ['Jewell',40,'cantora'],
                 ['Teriana',21,'Fitness']]

#print(dadosPessoais[0][0])
#print(len(dadosPessoais))

dadosPessoais[0][0] = 'DIDO'

for x in range(len(dadosPessoais)):
    for y in range(len(dadosPessoais[x])):
        print(dadosPessoais[x][y],end=' ')
    print('\n')
