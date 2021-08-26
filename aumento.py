#Faça um programa que leia o salário de um funcionario. Se ele receber mais de 1.250,00 ele recebe um aumento de 10%, caso receba menos ou igual a 1.250,00 ele recebe um aumento de 15%.

salario = float(input('Digite o valor do seu salário: '))
dez = (10*salario/100)+salario 
quinze = (15*salario/100)+salario
if salario > 1.250:
    print('==='*20)
    print(f'Você recebeu um aumento de 10% 🤩! Seu novo salário é {dez}')    
if salario <= 1.250:
    print('==='*20)
    print(f'Você recebeu um aumento de 15% 🤩! Seu novo salário é {quinze}')    
    
