#programa que lê vários números inteiros pelo teclado e no fim do programa mostre a média entre eles
#qual é o valor menor e maior entre os valores lidos. O programa deve perguntar se o usuário quer 
#ou não continuar a digitar valores.

numero = 0
usuario = ''
media = 0
contador = 0
soma = 0
maior_numb = 0
menor_numb= 3000000
while usuario != 'N':
    numero = int(input('Digite um número: '))
    usuario = input('Você deseja adicionar mais números? [S/N]: ').upper()
    contador+=1
    soma += numero
    media = soma/contador
    if numero > maior_numb:
        maior_numb = numero
    if numero < menor_numb:
        menor_numb = numero
print(f'Você digitou {contador} números')        
print(f'A média de todos os números é: {media}')    
print(f'O maior numero  é: {maior_numb}')
print(f'O menor numero é: {menor_numb}')    