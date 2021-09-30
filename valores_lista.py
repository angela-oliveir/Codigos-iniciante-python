#programa que leia 5 valores numéricos e guarde em uma lista.
#No final mostre o maior e menor valor digitado e suas respectivas posições na lista 

lista =[]
for c in range(1, 6):
    num1 = int(input('Digite um número: '))
    lista.append(num1)
maior = max(lista)
menor = min(lista)
pos_maior = lista.index(maior)
pos_menor = lista.index(menor)
print(lista)
print(f'O maior valor é {maior} que está na {pos_maior}ª posição')
print(f'O menor valor é {menor} que está na {pos_menor}ª posição')