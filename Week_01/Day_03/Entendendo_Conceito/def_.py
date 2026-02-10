# 🎯 Primeiro: 3 Exercícios Resolvidos (para você entender a dinâmica)

# Exercício Resolvido 1: Validador de Senha (Fácil)
# Descrição:
# Crie uma função que valide se uma senha atende aos critérios mínimos:

# Pelo menos 8 caracteres
# Contenha pelo menos um número
# Retorne True se válida, False caso contrário


def validar_senha(senha):
    """
    Valida se a senha atende aos critérios mínimos de segurança.
    
    Args:
        senha (str): A senha a ser validada
        
    Returns:
        bool: True se válida, False caso contrário
    """


    if len(senha) < 8:
        return False

    tem_numero = False

    for caractere in senha:
        if caractere in '0123456789':
            tem_numero = True
            break
    return tem_numero



# Testes
print(validar_senha("abc123"))        # False (menos de 8 caracteres)
print(validar_senha("abcdefgh"))      # False (sem número)
print(validar_senha("senha1234"))     # True
print(validar_senha("Python2024!"))   # True
print(validar_senha("portugues1"))  # False


# Exercício Resolvido 2: Calculadora de Desconto Progressivo (Médio)
# Descrição:
# Crie uma função que calcule o preço final de um produto com desconto progressivo:

# Compras até R$ 100: sem desconto
# Compras de R$ 100,01 até R$ 500: 10% de desconto
# Compras acima de R$ 500: 15% de desconto

# A função deve retornar uma tupla com (valor_original, desconto_aplicado, valor_final)


def calcular_desconto_progressivo(valor):
    """
    Calcula o desconto progressivo baseado no valor da compra.
    
    Args:
        valor (float): Valor original da compra
        
    Returns:
        tuple: (valor_original, desconto_aplicado, valor_final)
    """

    desconto = 0

    if valor <= 100:
        desconto = 0
    elif valor <= 500:
        desconto = 0.10
    else:
        desconto = 0.15
    
    valor_desconto = (valor * desconto)
    valor_final = (valor - valor_desconto)

    return (valor, valor_desconto, valor_final)


def exibir_resultado(valor):
    original, desconto, final = calcular_desconto_progressivo(valor)
    print(f'Valor original: R$ {original:.2f}')
    print(f'Desconto: R$ {desconto:.2f}')
    print(f'Valor final: R$ {final:.2f}')
    print('-' * 40)

exibir_resultado(80)  # Sem desconto
exibir_resultado(250) # 10% desconto ## 225 - R$ 25,00
exibir_resultado(500) # 15% desconto R$ 425,00 - R$ 50.00


# Exercício Resolvido 3: Analisador de Frequência de Palavras (Difícil)
# Descrição:
# Crie uma função que receba um texto e retorne as 3 palavras mais frequentes e suas contagens.

# Ignore palavras com menos de 3 letras
# Ignore maiúsculas/minúsculas
# Retorne uma lista de tuplas [(palavra, frequência), ...]


def analisar_frequencia_palavras(texto, top_n=3):
    """
    Analisa a frequência de palavras em um texto.
    
    Args:
        texto (str): O texto a ser analisado
        top_n (int): Quantidade de palavras mais frequentes a retornar
        
    Returns:
        list: Lista de tuplas (palavra, frequência) ordenadas por frequência
    """
    # Normaliza o texto
    texto = texto.lower()
    
    # Remove pontuação comum
    for pontuacao in '.,!?;:':
        texto = texto.replace(pontuacao, '')
    
    # Separa em palavras
    palavras = texto.split()
    
    # Filtra palavras com menos de 3 letras
    palavras_validas = []
    for palavra in palavras:
        if len(palavra) >= 3:
            palavras_validas.append(palavra)
    
    # Conta frequências
    frequencias = []
    palavras_contadas = []
    
    for palavra in palavras_validas:
        if palavra not in palavras_contadas:
            contador = 0
            for p in palavras_validas:
                if p == palavra:
                    contador += 1
            frequencias.append((palavra, contador))
            palavras_contadas.append(palavra)
    
    # Ordena por frequência (bubble sort simplificado)
    for i in range(len(frequencias)):
        for j in range(i + 1, len(frequencias)):
            if frequencias[j][1] > frequencias[i][1]:
                frequencias[i], frequencias[j] = frequencias[j], frequencias[i]
    
    # Retorna apenas o top_n
    resultado = []
    for i in range(min(top_n, len(frequencias))):
        resultado.append(frequencias[i])
    
    return resultado


# Teste
texto_exemplo = """
Python é uma linguagem incrível. Python é fácil de aprender.
Aprender Python pode abrir muitas portas. A comunidade Python é muito acolhedora.
"""

resultado = analisar_frequencia_palavras(texto_exemplo)
print("Top 3 palavras mais frequentes:")
for palavra, freq in resultado:
    print(f"'{palavra}': {freq} vezes")