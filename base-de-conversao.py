numero = int(input('Digite um número inteiro: '))
print('''Escolha uma opção: 
[1] BINARIO
[2] HEXADECIMAL
[3] OCTAL''')
opcao = int(input('Escolha uma opção: '))
binario = bin(numero)
hexadecimal = hex(numero)
octal = oct(numero)
if opcao == 1:
    print(f'O número Binario é: {binario}')
elif opcao == 2:
    print(f'O número Hexadecimal é: {hexadecimal}')
elif opcao == 3:    
    print(f'O número Octal é: {binario}')
else:
    print('===x'*15)
    print('Escolha uma das opções acima.')



    

