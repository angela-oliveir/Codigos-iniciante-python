#Faça um programa que leia dois números inteiros e diga se o primeiro ou o segundo é o valor maior #se forem iguais, mostre uma mensagem dizendo que são númenos iguais. 

print('¨¨¨¨¨'*15)
print('Veja qual é o maior valor de dois números digitando eles abaixo 😉')
print('¨¨¨¨¨'*15)
n1 = int(input('Digite o primeiro número: '))
n2 =int(input('Digite o segundo número: '))
if n1>n2:
    print(f'{n1} o PRIMEIRO valor é MAIOR')
elif n2>n1:
    print(f'{n2} o SEGUNDO valor é MAiOR')
elif n1==n2:
    print('Os dois números são iguais')