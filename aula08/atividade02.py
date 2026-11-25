numeros = []

while True:
    numero = int(input('\nInforme um número inteiro: '))
    numeros.append(numero)
    resposta = input("\nDeseja continuar [S/N] ? ").upper()[0]
    if resposta == "N":
        break

quantidade = len(numeros)
soma = sum(numeros)
lista_ordenada = sorted(numeros)

print(f'\nNúmeros computados: {numeros}')
print(f'Quantidade de números: {quantidade}')
print(f'Somatório dos números: {soma}')
print(f'Números ordenados: {lista_ordenada}')