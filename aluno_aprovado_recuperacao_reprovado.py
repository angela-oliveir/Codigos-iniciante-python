#Faça um programa que leia duas notas de um aluno e calcule sua média 
#mostrando uma mensagem no final de acordo com a média atingida.
#média abaixo de 5.0 Reprovado
#média entre 5.0 e 6.9 Recuperação
#média 7.0 ou superior Aprovado.
 
nota1= float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media_total = (nota1 + nota2)/2

#para descobrir se esta reprovado
if media_total < 5.0:
    print(f'Sua média é: {media_total}. \nVocê está REPROVADO!')

#Para descobrir se esta em recuperação 
elif media_total == 5.0 or media_total <= 6.9:
    print(f'Sua média é: {media_total}. \nVocê está em RECUPERAÇÃO!')

#Para descobrir se esta aprovado
elif media_total >= 7.0:
    print(f'Sua média é: {media_total}. \nVocê está APROVADO!')
