# 💚 Exercício 1: Dobrar Números com Lambda
# Descrição:
# Crie uma função lambda que receba um número e retorne o dobro dele. Depois use map() para aplicar essa lambda em uma lista de números.
# Requisitos:

# Use lambda para criar a função de dobrar
# Use map() para aplicar em uma lista
# Converta o resultado para lista


dobrar = lambda x: x * 2 # Função anônima  = def dobrar(x) -> return x * 2


numeros = [1,2,3,4,5] # Lista 
resultado = list(map(dobrar, numeros))


print(f'Original: {numeros}')
print(f'Dobrados: {resultado}')


resultado_direto = list(map(lambda x: x * 2, [1,2,3,4,5]))
print(f'Direto: {resultado_direto}')

