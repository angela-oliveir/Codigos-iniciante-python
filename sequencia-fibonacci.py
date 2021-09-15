#programa que lê um numero int e mostre na tela os n primeiros termos da
#sequencia de fibonacci  

n = int(input('Quantos termos da sequencia voce quer na tela? '))
termo1 = 0
termo2 = 1
contador = 0
while contador != n:
    print(termo1)
    termo3 = termo1+termo2
    termo1 = termo2
    termo2 = termo3
    contador += 1
print('Fim')
