
# 💚 Exercício 1: Dictionary Comprehension Básico
# Descrição:
# Crie um dicionário usando dict comprehension onde a chave é um número de 1 a 5 e o valor é seu quadrado.
# Requisitos:

# Use dict comprehension: {chave: valor for ...}
# Números de 1 a 5
# Valor = número ao quadrado (x²)



#Dict comprehension básico

quadrados = {x: x**2 for x in range(1, 6)}

print(f'Dicionário: {quadrados}')

# 1. Criar dicionário a partir de duas listas

nomes = ["Ana", "João", "Maria"]
idades = [25, 30, 28]

pessoas = {nome: idade for nome, idade in zip(nomes, idades)}
print(f"Pessoas: {pessoas}")

# 2. Filtrar com condição

numeros = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(f'Quadrados dos pares: {numeros}')


# 3. Transformar strings

frutas = ["maçã", "banana", "uva"]
tamanhos = {fruta: len(fruta) for fruta in frutas}
print(f"Tamanho das frutas: {tamanhos}")