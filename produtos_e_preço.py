#Crie uma tupla com nomes de produtos e seus respectivos preços na sequência
#No final, mostre seus respectivos preços organizando os dados em forma tabular


produtos_valores = ('Lápis', 1.75, 'Borracha', 2.0, 'Caderno', 15.90, 'Estojo', 25.0, 'Marcador', 7.40,)
print(f'='*40)
print(f'{"PRODUTOS E PREÇOS":^40}')
print(f'='*40)

for quant in range(len(produtos_valores)):
    if quant %2==0:
        print(f'{produtos_valores[quant]:.<30}', end='')
    elif quant %2==1:
        print(f'R${produtos_valores[quant]:>6.2f}')    
    

