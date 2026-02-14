# 🧡 Exercício 4: Inverter Chaves e Valores com Dict Comprehension
# Descrição:
# Dado um dicionário de produtos e preços, use dict comprehension para criar um novo dicionário onde preços são chaves e produtos são valores.
# Requisitos:

# Dicionário original: {"arroz": 20.50, "feijão": 8.90, "macarrão": 5.50, "açúcar": 4.20}
# Use dict comprehension
# Inverta chave ↔ valor



original = {"arroz": 20.50, "feijão": 5.50, "macarrão": 5.51, "açúcar": 4.20}


for produto, preco in original.items():
    print(produto, preco)

invertido = {preco: produto for produto, preco in original.items()}
print(invertido)
