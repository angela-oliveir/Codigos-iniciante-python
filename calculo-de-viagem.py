viagem = float(input('Digite a distancia da sua viagem em km: '))
km1 = (viagem * 0.50)
km2 = (viagem * 0.45)
if viagem <= 200.0:
    print(f'Sua viagem é menor ou igual a 200km. Sua passagem custa {km1}')
else: 
    print(f'Sua viagem é mais longa que 200km. Sua passagem custa {km2}')