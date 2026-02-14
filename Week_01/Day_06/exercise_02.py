# 🧡 Exercício 2: Set Comprehension e Remoção de Duplicatas
# Descrição:
# Use set comprehension para criar um conjunto com os comprimentos únicos de palavras em uma frase.
# Requisitos:

# Receba uma frase
# Use set comprehension
# Pegue apenas tamanhos únicos das palavras




frase = "python é uma linguagem de programação muito poderosa e simples"


tamanhos_unicos = {len(palavra) for palavra in frase.split()}

print(f"Frase: {frase}")
print(f"Tamanhos únicos: {tamanhos_unicos}")
print(f"Quantidade de tamanhos diferentes: {len(tamanhos_unicos)}")