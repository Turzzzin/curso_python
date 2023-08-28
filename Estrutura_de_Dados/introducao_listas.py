cidade1 = 'Rio de Janeiro'
cidade2 = 'São Paulo'
cidade3 = 'Salvador'
#                -4              -3          -2          -1
cidades = ['Rio de Janeiro', 'São Paulo', 'Salvador', 'Goiania']
#                 0               1           2           3
print(cidades)

cidades[0] = 'Brasilia'
print(cidades)

cidades.append('Santa Catarina')
print(cidades)

cidades.remove('Salvador')
print(cidades)

cidades.insert(2, 'São Caetano')
print(cidades)

cidades.pop(0)
print(cidades)

cidades.sort()
print(cidades)