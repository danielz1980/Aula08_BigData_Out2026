numeros = []
numeros_ordenados = []

for i in range(3):
    numero = int(input('Informe um número inteiro: '))
    numeros.append(numero)

numeros_ordenados = sorted(numeros)

conjunto = set(numeros_ordenados)  # converte uma lista para um conjunto

print(f'\nNúmeros computados com repetição: {numeros_ordenados}')

print(f'\nNúmeros computados sem repetição: {conjunto}')
