# 🧡 Exercício 3: Generator de Fibonacci
# Descrição:
# Crie um generator fibonacci(limite) que gere números da sequência de Fibonacci até o limite.
# Requisitos:

# Use yield
# Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13...
# Pare quando passar do limite

def fibonacci(limite):
    a, b = 0, 1
    
    while a <= limite:
        yield a
        a, b = b, a + b


for numero in fibonacci(15):
    print(numero)