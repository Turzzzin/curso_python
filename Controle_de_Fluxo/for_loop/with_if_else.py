compra_confirmada = True
dados_compra = 'Compra no valor de R$12.50 confirmada'

for enviar in range(3):
    if compra_confirmada:
        print(dados_compra)
        print('Detalhes enviados para o seu e-mail.')
        break
else:
    print("Falha na compra")