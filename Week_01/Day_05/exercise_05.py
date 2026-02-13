
# ### 🧡 **Exercício 5: Filtrar Nomes Curtos**

# **Descrição:**  
# Dada uma lista de nomes, use `filter()` para pegar apenas nomes com 5 ou menos letras.

# **Requisitos:**
# - Lista: `["Ana", "João", "Maria", "Pedro", "Fernanda", "Carlos", "Bia"]`
# - Use `filter()` com lambda
# - Converta para lista

# **Saída esperada:**
# ```
# Nomes curtos: ['Ana', 'João', 'Maria', 'Pedro', 'Bia']


nomes = ["Ana", "João", "Maria", "Pedro", "Fernanda", "Carlos", "Bia"]

nomes_curtos = list(filter(lambda nome: len(nome) <= 5, nomes))

print("Nomes curtos:", nomes_curtos)
