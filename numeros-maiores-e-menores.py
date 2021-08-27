#Faça um programa que leia 3 números e diga qual é o maior e menor numero.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
#Para descobrir se um numero é maior
maior = n1
if n2>maior:
    maior = n2
if n3>maior:
    maior = n3
    print(f'{maior} é o MAIOR numero')
#Para descobrir o numero menor
menor = n1
if n2<menor:
    menor = n2
if n3<menor:
    menor = n3
    print(f'{menor} é o MENOR numero')

    