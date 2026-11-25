produtos = []

for i in range(5):
    produto = input('Informe o nome do produto: ')
    produtos.append(produto)  # adiciona na lista produtossssss

print(produtos)

# Acesso ao elemento
n = int(input('Digite a posição do elemento a acessar: '))  # 2
print(produtos[n-1])  # 1

# Alterando uma lista "nome de um elemento"
produtos[n-1] = input(f'Informe o novo nome do produto {n}: ')  # 2
print(produtos)

# Remover da lista
produto_a_remover = input('\nDigite o nome do produto a remover: ')

if produto_a_remover in produtos:
    produtos.remove(produto_a_remover)
print(produtos)

# Pesquisar os métodos insert, pop(), clear