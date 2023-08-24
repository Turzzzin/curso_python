# Realiza uma tarefa
def cliente1(nome):
    print(f'Olá {nome}')

cliente1('Maria')

# Guarda o resultado (retorna)
def cliente2(nome):
    return f'Olá {nome}'

print(cliente2('José'))

x = cliente1('Maria')
y = cliente2('José')

print(x)
print(y)