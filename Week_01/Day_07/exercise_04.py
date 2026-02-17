# 🧡 Exercício 4: Conversor com Múltiplas Exceções
# Descrição:
# Crie função acessar_lista(lista, indice) que retorne elemento de uma lista tratando erros.
# Requisitos:

# Use try/except
# Trate IndexError (índice inválido)
# Trate TypeError (não é lista)
# Retorne valor ou mensagem de erro apropriada

def acessar_lista(lista, indice):
    try:
        return lista[indice]
    
    except IndexError:
        return "Erro: índice fora do alcance da lista."
    
    except TypeError:
        return "Erro: objeto não é uma lista ou índice inválido."

print(acessar_lista([10, 20, 30], 1))