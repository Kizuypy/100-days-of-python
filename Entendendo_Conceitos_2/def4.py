# 🧡 EXERCÍCIO RESOLVIDO 3: Mesclador de Dicionários com Contagem
# Contexto: APIs frequentemente retornam dados que precisam ser mesclados.
# Tarefa: Crie uma função que mescle dois dicionários de produtos somando as quantidades se a chave já existir.



def mesclar_estoque(estoque1, estoque2):

    # Usa .copy() para não modificar o original (shallow copy)
    resultado = estoque1.copy()
    
    # Percorre o segundo dicionário
    for produto, quantidade in estoque2.items():
        # Se o produto já existe, soma as quantidades
        if produto in resultado:
            resultado[produto] += quantidade
        else:
            # Se não existe, adiciona novo produto
            resultado[produto] = quantidade
    
    return resultado


# 🧪 TESTES
print("=== MESCLADOR DE ESTOQUE ===")

estoque_loja1 = {
    'notebook': 5,
    'mouse': 20,
    'teclado': 15
}

estoque_loja2 = {
    'mouse': 10,
    'teclado': 5,
    'monitor': 8
}

estoque_total = mesclar_estoque(estoque_loja1, estoque_loja2)
print("Estoque mesclado:")
for produto, qtd in estoque_total.items():
    print(f"  {produto}: {qtd} unidades")

# Saída:
# notebook: 5 unidades
# mouse: 30 unidades (20 + 10)
# teclado: 20 unidades (15 + 5)
# monitor: 8 unidades