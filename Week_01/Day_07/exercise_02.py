# 💚 Exercício 2: Divisão Segura
# Descrição:
# Crie uma função dividir_seguro(a, b) que divida dois números tratando divisão por zero.
# Requisitos:

# Use try/except
# Capture ZeroDivisionError
# Se erro, retorne None e mostre mensagem
# Se sucesso, retorne o resultado

def dividir_seguro(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print('ERRO: divisão por zero não é permitida!')
        return None


div = dividir_seguro(20, 2)
print(div)