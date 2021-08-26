#Faça um programa que leia três lados e diga se da para transformar ou não em um triângulo.

print('####'*15)

print('Digite três lados para saber se formam ou não um triângulo')

print('####'*15)

a = float(input('Primeiro lado: '))
b = float(input('segundo lado: '))
c = float(input('terceiro lado: '))
if (a==b and a<c) or (a==c and a<b) or (b==c and b<a):
    print('Você formou um triângulo')
else: 
    print('Você NÃO formou um triângulo') 
    
    
