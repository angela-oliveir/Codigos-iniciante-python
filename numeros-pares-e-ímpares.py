inteiro = float(input('Digite um numero que te digo se é par ou ímpar: '))
resultado = inteiro % 2
print('==' *10)
print('Analizando resultado')
print('==' *10)
if resultado == 0:  
    print('O numero é par')
else:
    print('O numero é ímpar')