#Programa que leia três lados e diga se é um triângulo equilátero, escaleno ou isósceles

print('####'*15)

print('Digite três lados para saber se formam ou não um triângulo')

print('####'*15)

a = float(input('Primeiro lado: '))
b = float(input('segundo lado: '))
c = float(input('terceiro lado: '))

#isoscélis são dois lados iguais

if (a==b and a<c) or (a==c and a<b) or (b==c and b<a):
    print('Você formou um triângulo ISÓSCELES')
    
#Equilatero tem todos os lados iguais
elif (a == b and a == c and b == c):
    print('Você formou um triângulo EQUILÁTERO')

#Escaleno tem todos os lados diferentes

elif (a != b and a != c and b != c):
    print('Esse é um triângulo ESCALENO')
    

    
    
