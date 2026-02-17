# 💚 Exercício 1: Generator de Countdown
# Descrição:
# Crie um generator countdown(n) que faça contagem regressiva de n até 0.
# Requisitos:

# Use yield
# Comece em n e vá até 0
# Teste com for loop

def countdown(n):
    while n >= 0:
        yield n
        n -= 1

for num in countdown(5):
    print(num)