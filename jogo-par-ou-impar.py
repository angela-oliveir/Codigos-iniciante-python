#programa que joga par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
#mostrando o total de vitorias consecutivas que ele conquistou no final do jogo.

from random import randint
from time import sleep
tipo = '' 
pc = usuario = vitoria = 0
print('*=*=*'*10)
print('VAMOS JOGAR PAR OU ÍMPAR?')
print('*=*=*'*10)
while True:
    tipo = str(input('Você escolher PAR ou Ímpar? [P/I]: ')).lower()
    usuario = int(input('Digite um número: '))
    pc = randint(0, 11)
    total = (usuario + pc)
    while tipo != 'p' and tipo != 'i':
        tipo = str(input('Você escolhe PAR ou ÌMPAR? [P/I]: ')).lower()
    print(f'Você escolheu {usuario} e o computador escolheu {pc}\nO Total é: {total}')     
    if tipo == 'p':
        if total % 2 == 0:
            vitoria += 1
            print('Você VENCEU!')
        else:
            print('Você PERDEU!')
            print(f'GAME OVER! Você venceu {vitoria} vezes.')
            break
    elif tipo == 'i' :
        if total % 2 == 1:
            vitoria += 1
            print('Você VENCEU!')
        else:
            print('Você PERDEU!')
            print(f'GAME OVER! Você venceu {vitoria} vezes')
            break   
print('Vamos jogar novamente...')        

    
    