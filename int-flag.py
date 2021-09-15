#Programa que lê varios números inteiros pelo teclado, o programa só vai parar quando o usuarios 
#digitar 999, que é a condição de parada. No final mostre quantos números foram digitados e qual 
#é a soma entre eles (disconsiderando o flag)
soma = 0
contador = 0
numero = 0
n = ''
while numero != 999:
    numero = int(input('Digite vários números aleatorios: '))
    contador += 1
    soma += numero
soma -= 999    
contador -= 1
print(f'Você digitou {contador} números. Soma {soma} Fim')    
