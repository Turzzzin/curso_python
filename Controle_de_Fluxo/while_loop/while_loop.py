valor = 100
dia = 0
while valor > 20:
    dia += 1
    if dia < 10:
        print(f'No dia 0{dia} o produto será vendido por R${valor},00')
    else:
        print(f'No dia {dia} o produto será vendido por R${valor},00')
    
    valor -= 5