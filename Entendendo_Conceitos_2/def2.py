# 💚 EXERCÍCIO RESOLVIDO 1: Contador de Vogais com DicionárioContexto: Análise de texto é comum em processamento de linguagem natural.Tarefa: 
# Crie uma função que conte quantas vezes cada vogal aparece em um texto.


def contar_vogais(texto):
    #  """
    # Conta a frequência de cada vogal em um texto.
    
    # Args:
    #     texto (str): Texto a ser analisado
        
    # Returns:
    #     dict: Dicionário com vogais e suas contagens
    # """
    vogais = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}


    texto = texto.lower()

    for letra in texto:
        if letra in vogais:
            vogais[letra] += 1
    return vogais


print("=== CONTADOR DE VOGAIS ===")
resultado = contar_vogais("Python é uma linguagem incrível")
print(resultado)
# Saída: {'a': 3, 'e': 3, 'i': 3, 'o': 1, 'u': 2}

print("\nVogais encontradas:")
for vogal, quantidade in resultado.items():
    print(f"Letra '{vogal}': {quantidade} vez(es)")