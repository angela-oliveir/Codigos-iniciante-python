#Programa que lê um número qualquer e mostre seu fatorial 


resultado = 1
contador = 1
numero = int(input('Fatorial de: '))
while contador <= numero:
    resultado *= contador
    contador += 1
print(f'O fatorial de {numero} é: {resultado}')