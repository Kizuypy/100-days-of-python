# 🧡 MÉDIO 2: Agrupador de Palavras por Tamanho
# Contexto: Análise de texto agrupa dados por características.
# Tarefa: Crie uma função agrupar_por_tamanho(palavras) que:

# Receba uma lista de palavras
# Retorne um dicionário onde:

# Chave = tamanho da palavra
# Valor = lista de palavras com aquele tamanho


def agrupar_por_tamanho(palavras):
    lista = {}

    for palavra in palavras:
        tamanho = len(palavra)
        if tamanho in lista:
            lista[tamanho].append(palavra)
        else:
            lista[tamanho] = [palavra]

    return lista

palavras = ["python", "java", "c", "ruby", "go", "javascript", "sql"]
print(agrupar_por_tamanho(palavras))