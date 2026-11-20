numeros = []
numeros_ordenados = []

for i in range(3):
    numero = int(input('Informe um número inteiro: '))
    numeros.append(numero)

total = sum(numeros)
numeros_ordenados = sorted(numeros)

print(f'\nNúmeros computados: {numeros}')
print(f'\nNúmeros ordenados crescentemente: {numeros_ordenados}')
print(f'\nSomatório dos números: {total}')