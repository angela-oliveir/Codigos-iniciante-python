#Faça uma tabuada usando o laço de repetição for

from time import sleep
tabuada = int(input('Digite um numero: '))
print('Carregando tabuada...')
sleep(2)
for c in range(1, 11):
    resultado = (tabuada*c)
    sleep(1)
    print(f'{tabuada} X {c} = {resultado}')
    sleep(1)
print('Fim')






