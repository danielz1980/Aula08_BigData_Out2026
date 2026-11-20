vendas = []

for i in range(3):
    venda = float(input('Informe o valor da venda: '))
    vendas.append(venda)

total = sum(vendas)

print(f'\nVendas computadas: {vendas}')
print(f'\nTotal das vendas: {total}')



