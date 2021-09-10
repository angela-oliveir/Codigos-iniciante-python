#programa que lê nome idade e sexo de 4 pessoas e mostre no fim
#média de idade do grupo
#qual o nome do homem mais velho
#quantas mulheres tem menos de 20 anos
from time import sleep
media_grupo = 0
idade_velho = 0
nome_velho = ''
quantidade_de_pessoas = 4
mulher_vinte = 0
for c in range(1, quantidade_de_pessoas+1):
    print(f'=========== {c}ª PESSOA ==========')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Qual opção você se identifica [M/F]: '))
    
    media_grupo = (media_grupo + idade)
    media = (media_grupo/quantidade_de_pessoas) 
    if sexo in 'Mm' and idade > idade_velho:
        idade_velho = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        mulher_vinte += 1
print('-=-=-=-=-=-=-=-=- RESULTADO -=-=-=-=-=-=-=-=-=-=')
sleep(1)
print(f'A média de idade do grupo é de {media}')
print(f'Homem mais velho se chama {nome_velho}, ele tem {idade_velho} anos')
print(f'No grupo existe {mulher_vinte} pessoas menores de 20 anos.')