produtos = []

for i in range(3):
    produto = input('Informe o nome do produto: ')
    produtos.append(produto)

print(produtos)
print()

# # Acessando um elemento
# n = int(input('Digite a posição do elemento a acessar: '))
# print(produtos[n-1])

# # Alterando os elementos da lista
# produtos[n-1] = input(f'Informe o novo nome do elemento na posição {n}: ')
# print(produtos)

# Removendo um elemento da lista
produto_a_remover = input('Digite o nome do produto a remover: ')

if produto_a_remover in produtos:
    produtos.remove(produto_a_remover)
else:
    print('\nProduto não identificado')

print()
print(produtos)

# Outros métodos: insert, pop, clear, count