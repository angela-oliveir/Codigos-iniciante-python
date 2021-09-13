#programa que leia dois valores e mostre um menu na tela:
#[1] somar
#[2] multiplicar
#[3] maior 
#[4] novos números 
#[5] sair do programa
#O programa deverá realizar a operação solicitada em cada caso.
from time import sleep
opcao = 0
while opcao != 5: 
    valor1 = int(input('Digite o 1º valor: '))
    valor2 = int(input('Digite o 2º valor: '))
    print('ESCOLHA UMA OPÇÃO: ')
    print('''
    [1] Somar os número
    [2] Multiplicar os números
    [3] Deseja saber qual o maior número
    [4] Deseja digitar outros números
    [5] Sair do programa''')
    opcao = int(input('Digite uma opção: ')) 
    sleep(1)
    if opcao == 1:
        opc1 = (valor1+valor2)
        print(f'A soma dos dois valores é: {opc1}')
        sleep(1)
    if opcao == 2:
        opc2 = (valor1*valor2)
        print(f'A multiplicação dos dois valores é: {opc2}')
        sleep(1)
    if opcao == 3:
        opc3 = max(valor1, valor2)
        print(f'O maior valor é {opc3}')
        sleep(1)
    if opcao == 4:
        continue
        sleep(1)
       