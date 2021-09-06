#Programa que lê o primeiro termo e a razão de uma PA. No final mostre os 10 primeiros termos 
#dessa progressão.

n1 = int(input('Digite o primeiro elemento: '))
razao = int(input('Digite a razão: '))
calculo = (n1 + (10-1)*razao)
calculo = (calculo + 1) 

for c in range(n1, calculo, razao):
    print(c)
print('Esses são os 10 primeiros termos da PA')    







