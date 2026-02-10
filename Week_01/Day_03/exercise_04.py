
# Exercício 4: Gerador de Estatísticas de Lista
# Descrição:
# Crie uma função estatisticas_lista(numeros) que receba uma lista de números e retorne um dicionário com estatísticas.
# Requisitos:

# Calcule: soma, média, maior valor, menor valor, quantidade de pares, quantidade de ímpares
# Retorne um dicionário com as chaves: 'soma', 'media', 'maior', 'menor', 'pares', 'impares'
# A média deve ter 2 casas decimais
# Se a lista estiver vazia, retorne None

# Exemplo de uso:
# pythonnumeros = [10, 5, 8, 3, 15, 2, 9]
# print(estatisticas_lista(numeros))
# # {'soma': 52, 'media': 7.43, 'maior': 15, 'menor': 2, 'pares': 3, 'impares': 4}
# ```

# **Dica:** Use loops para calcular cada estatística separadamente.

numeros = []

def estatisticas_lista(numeros):
    if not numeros:
        return None
    
    soma = 0
    maior = numeros[0]
    menor = numeros[0]
    pares = 0
    impares = 0

    for numero in numeros:
        soma += numero

        if numero > maior:
            maior = numero

        if numero < maior:
            menor = numero

        if numero % 2 == 0:
            pares +=1
        else:
            impares += 1
    media = round(soma / len(numeros), 2)

    return {
        soma: soma,
        media: media,
        maior: maior,
        menor: menor,
        pares: pares,
        impares: impares
    }

print(estatisticas_lista(numeros))
    