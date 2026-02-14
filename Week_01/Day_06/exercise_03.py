# 🧡 Exercício 3: Verificador de Tipos com isinstance()
# Descrição:
# Crie uma função que receba uma lista com valores mistos e separe por tipo usando isinstance().
# Requisitos:

# Função recebe lista com tipos variados
# Use isinstance() para verificar tipos
# Retorne dicionário com tipos separados


def separar_por_tipo(lista):
    resultado = {
        'inteiros' : [],
        'floats' : [],
        'strings' : [],
        'booleanos' : [],
        'listas' : [],
        'outros': []
    }

    for item in lista:
        if isinstance(item, bool):
            resultado['booleanos'].append(item)
        elif isinstance(item, int):
            resultado['inteiros'].append(item)
        elif isinstance(item, float):
            resultado['floats'].append(item)
        elif isinstance(item, str):  
            resultado['strings'].append(item)
        elif isinstance(item, list):
            resultado['listas'].append(item)
        else:
            resultado['outros'].append(item)

    return {tipo: valores for tipo, valores in resultado.items() if valores}



dados_mistos = [10, 3.14, "python", True, [1, 2], 42, "java", False, 2.71, [3, 4]]

separados = separar_por_tipo(dados_mistos)

print("Dados separados por tipo:")
for tipo, valores in separados.items():
    print(f"{tipo}: {valores}")