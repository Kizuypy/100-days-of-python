# 🟡 EXERCÍCIOS MÉDIOS
# Exercício 3: Sistema de Caixa Eletrônico
# Descrição:
# Crie uma função sacar_dinheiro(valor) que retorne a quantidade mínima de cédulas necessárias para um saque.
# Requisitos:

# Cédulas disponíveis: 100, 50, 20, 10, 5, 2
# Retorne um dicionário com as cédulas usadas: {100: x, 50: y, ...}
# Só inclua no dicionário as cédulas efetivamente usadas
# Se o valor não puder ser sacado (ex: 3 reais), retorne None

# Exemplo de uso:
# pythonprint(sacar_dinheiro(186))  # {100: 1, 50: 1, 20: 1, 10: 1, 5: 1}
# print(sacar_dinheiro(73))   # {50: 1, 20: 1, 2: 1}
# print(sacar_dinheiro(3))    # None
# Dica: Use um loop para iterar pelas cédulas em ordem decrescente e divida o valor restante.


def sacar_dinheiro(valor):
    cedulas = [100, 50, 20, 10, 5, 2]
    resultado = {}

    for cedula in cedulas:
        quantidade = valor // cedula
        if quantidade > 0:
            resultado[cedula] = quantidade
        
            valor = valor % cedula
    if valor  != 0:
        return None
    return resultado


print(sacar_dinheiro(180))
