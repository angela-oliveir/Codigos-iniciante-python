#Faça um programa que leia o ano de nascimento de um jovem
#e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
#se é a hora exata de se alistar ou se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

ano_de_nascimento = int(input('Digite o ano do seu nascimento: '))
idade = (2021 - ano_de_nascimento)
print(f'Você tem {idade} anos') 

#Para descobrir quanto tempo falta para o alistamento
if idade < 18:
    ano_que_falta_alistar = 18 - idade
    print(f'Faltam {ano_que_falta_alistar} anos para você se alistar')
    
#Para descobrir quanto tempo passou da idade do alistamento
elif idade > 18:
    ano_que_passou_do_alistamento = idade - 18
    print(f'Já se passaram {ano_que_passou_do_alistamento} para seu alistamento.')
    
#Para mostrar se é a hora exata para alistar
elif idade == 18:
    print('Você já pode se alistar. Procure a junta militar do seu município. ')

