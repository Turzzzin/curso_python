def soma(num1, num2):
    resultado = num1 + num2
    # As variáveis dentro de funções não são globais.
    print(resultado)

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um numero: "))

soma(num1, num2)