#programa que lê uma frase e diz se é ou não um palíndromo desconsiderando espaços. 
 
frase = str(input('Digite uma frase : ')).strip().upper()  

palavras = frase.split()  
junto = ''.join(palavras) 
inverso = ''
for l in range(len(junto) -1, -1, -1):
    inverso += junto[l]
print(f'O inverso de {junto} é {inverso}')    
if inverso == junto:
    print('TEMOS um palíndromo')
else: 
    print('NÃO temos um palíndromo') 
        
        
