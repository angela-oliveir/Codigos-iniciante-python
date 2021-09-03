#Programa que leia seis número inteiros e mostre a soma apenas daqueles que forem numeros pares, se #for ímpar, desconsidere-o. 

soma = 0
contador = 0
for c in range(1, 7):
    number = int(input(f'Digite o {c}º número: '))
    if number % 2 == 0:
        soma += number
        contador += 1
print(f'Você informou {contador} PARES. \nA a soma entre eles é: {soma}')
