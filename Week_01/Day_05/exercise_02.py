# 💚 Exercício 2: Filtrar Números Pares
# Descrição:
# Use filter() com lambda para filtrar apenas os números pares de uma lista.
# Requisitos:

# Use lambda para verificar se é par
# Use filter() para filtrar
# Converta o resultado para lista





pares = lambda x: x % 2 == 0

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

resultado = list(filter(pares, numeros))

resultado_direto = list(filter(lambda x: x % 2 == 0, [1,2,3,4,5,6,7,8]))

print(f'Direto: {resultado_direto}')

print(f'Os Pares são: {resultado}')