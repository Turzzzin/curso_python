def soma(*numeros):
    resultado = 0
    for num in numeros:
        resultado += num
    return resultado

print (soma(2, 3, 4, 7))