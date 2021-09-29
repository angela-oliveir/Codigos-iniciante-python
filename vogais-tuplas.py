tupla = ('escola', 'livros', 'aprender', 'plantas', 'programas')
for p in tupla:
    print(f'\nNa palavra {p.upper()} temos as vogais:', end=' ')
    for vogais in p:
        if vogais in 'aeiou':
            print(vogais, end=' ')
