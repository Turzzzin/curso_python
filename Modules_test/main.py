from functions import Functions

num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))

print('Digite 1 para somar')
print('Digite 2 para subtrair')
print('Digite 3 para multiplicar')
print('Digite 4 para dividir')

inputUser = int(input())
if inputUser == 1:
    result = Functions.soma(num1, num2)
elif inputUser == 2:
    result = Functions.subtracao(num1, num2)
elif inputUser == 3:
    result = Functions.multiplicacao(num1, num2)
elif inputUser == 4:
    result = Functions.divisao(num1, num2)

print(result)