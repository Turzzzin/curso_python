def boas_vindas(nome, quantidade):
    print(f'Olá {nome}.')
    print(f'Temos {str(quantidade)} laptops em estoque')
    print('\n')

boas_vindas('Marcos', 5)

def boas_vindas_default(nome, quantidade=6): # A O DEFAULT É SEMPRE NO FINAL
    print(f'Olá {nome}.')
    print(f'Temos {str(quantidade)} laptops em estoque')
    print('\n')

boas_vindas_default('Marcos')