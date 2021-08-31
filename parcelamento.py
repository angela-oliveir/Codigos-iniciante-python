#Programa que calcula um valor a ser pago por um produto considerando seu preço normal 
#e condições de pagamento. 
#A vista\cheque: 10% desconto
#A vista no cartão: 5% desconto
#Em 2x no cartão: preço normal
#3x ou mais: 20% juros 


valor_produto = float(input('Digite o vaor do produto: '))
print('==='*15)
print('''
    Escolha entre as opções uma forma de pagamento:
       [1] A VISTA OU EM CHEQUE GANHE 20% DE DESCONTO
       [2] A VISTA NO CARTÃO GANHE 5% DE DESCONTO
       [3] PARCELE EM 2x NO CARTÃO SEM JUROS
       [4] PARCELE DE 3x Á 5x COM 20% JUROS 
    
    ''')

opcao_pagamento = int(input('Digite uma opção: '))


if opcao_pagamento == 1:
    valor_produto = valor_produto - (20*valor_produto/100)
    print(f'Você ganhou 20% de desconto na sua compra. \nO total de pagamento é: R${valor_produto}')

elif opcao_pagamento == 2:
    valor_produto = valor_produto - (5*valor_produto/100)
    print(f'Você ganhou 5% de desconto na sua compra. \nO total de pagamento é: R${valor_produto}')
    
elif opcao_pagamento == 3:
    valor_produto = (valor_produto/2)
    print(f'Você pode parcelar até 2x SEM JUROS. \nTotal de pagamento: 2x de R${valor_produto}')

elif opcao_pagamento == 4:
    print('''
        Escolha uma opção de parcelamento: 
          [1] Parcele em 3x
          [2] Parcele em 4x
          [3] Parcele em 5x  
    ''')
    
    opcao_parcelamento = int(input('Digite uma opção: '))
    
if opcao_parcelamento == 1:
    parcelamento = 3
        
elif opcao_parcelamento == 2:
    parcelamento = 4
        
elif opcao_parcelamento == 3:
    parcelamento = 5
    
    valor_produto = (valor_produto * (1+20/100)) / parcelamento
    print(f'Você parcelou em {parcelamento}x. \nValor da parcela: R${valor_produto}')
    

    
    
    



    
    