# 💛 EXERCÍCIO RESOLVIDO 2: Removedor de Duplicatas com Set
# Contexto: Em bancos de dados, precisamos remover registros duplicados.
# Tarefa: Crie uma função que remova itens duplicados de uma lista mantendo a ordem original.


from nt import remove


def remover_duplicatas(lista):
# Set para rastrear itens já vistos (busca rápida)
    vistos = set()
 # Lista para armazenar resultado final
    resultado = []
# Percorre cada item da lista original
    for item in lista:
# Se o item ainda não foi visto
        if item not in vistos:
            vistos.add(item) # Adiciona no set de controle 
            resultado.append(item) # Adiciona no resultado

    return resultado

print("=== Removedor de Duplicatas ===")

numeros = [1, 2, 3, 2, 4, 1, 5, 3, 6]

print(f"Original {numeros}")
print(f"Sem duplicatas: {remover_duplicatas(numeros)}")

nomes = ["Ana", "João", "Ana", "Maria", "João", "Pedro"]
print(f"\nOriginal: {nomes}")
print(f"Sem duplicatas: {remover_duplicatas(nomes)}")