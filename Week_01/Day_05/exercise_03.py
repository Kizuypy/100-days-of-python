# 🧡 Exercício 3: List Comprehension com Condição
# Descrição:
# Use list comprehension para criar uma lista com o quadrado de números ímpares de 1 a 10.
# Requisitos:

# Use list comprehension
# Aplique condição (apenas ímpares)
# Calcule o quadrado



quadrados_impares = [x ** 2 for x in range(11) if x % 2 != 0]

print(f"Quadrados dos ímpares: {quadrados_impares}")


maiores_que_5 = [x for x in range(11) if x > 5]

print(f'Números maiores que 5: {maiores_que_5}')