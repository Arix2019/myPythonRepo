# testa se uma frase é igual de tras pra frente
# ex: A SACADA DA CASA <--> ASAC AD ADACAS A

frase = 'o lobo ama o bolo'

if list(frase.upper().replace(' ','')) == list(reversed(frase.upper().replace(' ',''))):
    print('OK!!\n"{}" é um palindromo.'.format(frase))
else:
    print('Oops!!\n"{}" não é um palindromo.'.format(frase))

