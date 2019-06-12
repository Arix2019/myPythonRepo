'''
programa que tenha uma tupla unica com nomes de produtos e seus
respectivos preços na sequencia
mostre uma listagem de preços organizando dados em forma tabular.
'''
listagem = ('Tenis',1.355, 'Camisa',245.25, 'Calca',600.12, 'Bermuda',52.15, 'Cinto',182.00,
            'Meias',250.00, 'Jaqueta',1.255)

print('-'*41)
print(f'{"LISTAGEM DE PREÇO":=^41}') #centraliza o texto com quarenta espaços e preenche com (=).
print('-'*41)
for pos in range(0,len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='') #insere trinta espaços a esquerda e preenche com (pontos).
    else:
        print(f' R$:{listagem[pos]:>7.2f}') #insere sete espaços a direita com 2 casas decimais
print('-'*41)