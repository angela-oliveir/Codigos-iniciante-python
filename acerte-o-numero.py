#Jogo que o computador vai pensar em um numero de 0 a 10 e o jogador vai tentar 
#advinhar o número até acertar, mostrando no final
#quantos palpites foram necessários para o usuário vencer. 



from random import choice
from time import sleep
numero = choice(range(0,11))
n = None
contador = 0
print('=-=-=-='*10)
print('\nVamos jogar! 😃\n')
print('=-=-=-='*10)
print('Descubra qual o número de 0 á 10 que o computador está pensando... 🤯')
sleep(1)
while n != numero:
    contador += 1
    n = int(input('Digite um número: '))    
        
    if numero != n:
        print('Você ERROU! Tente novamente.')

print(f'Você ACERTOU!\nVocê fez {contador} tentativas.')    