# SETS "Conjuntos"
# Coleção mutável
# Não garante ordem
# Não há índice
# NÃO Permite elementos duplicados

# Criar sets vazios
dias = set()
dias.add('segunda')
dias.add('terça')
print(dias)


# Conjuntos inicializados
frutas = {'Maça', 'Uva', 'Pera', 'Laranja'}
print(frutas)
print(type(frutas))

# remover
# frutas.remove('Uva')
frutas.discard('Uva')
print(frutas)

print(len(frutas))

# # converter lista para sets
# lista = [5, 7, 4, 1, 2, 8, 13, 6]
# conjunto_set = set(lista)
# print(conjunto_set)

numeros = [5, 7, 4, 1, 4, 8, 13, 6, 5, 5, 13, 8, 29]  # lista
conjunto = set(numeros)  # converter lista para conjunto set
numeros = list(conjunto)  # converte conjunto set para lista
print(len(conjunto))
print(conjunto)