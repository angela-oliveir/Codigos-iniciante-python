#programa que calcula a soma de todos os números ímpares que são múltiplos de 3
#e que se encontram no intervalo de 1 á 500.



soma = 0
contador = 0
for numero in range(1, 501, 2):
    if numero % 3 == 0:
        soma = soma + numero
        contador = contador + 1
print(f'A soma de todos os {contador} valores é: {soma}')       




