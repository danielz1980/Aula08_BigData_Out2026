# SETS 'Conjunto'
# Coleção mutável
# Não há índice, consequentemente, não há posição
# Não aceita elementos repetidos

# dias = set()  # cria set vazio
# dias.add('segunda')
# dias.add('terça')
# print(dias)

# frutas = {'Maça', 'Uva', 'Pera', 'Banana'}  # conjuntos inicializados
# print(frutas)
# print(type(frutas))

# frutas.remove('Uva')
# # frutas.discard("Uva")
# print(frutas)
# print(len(frutas))

numeros = [5, 7, 4, 1, 2, 8, 13, 6, 6, 13]
conjunto = set(numeros)  # converte uma lista para um conjunto
numeros = list(conjunto)  # converte um conjunto para uma lista
print(conjunto)
print(len(conjunto))