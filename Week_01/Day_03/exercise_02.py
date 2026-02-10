# Exercício 2: Verificador de Palíndromo
# Descrição:
# Crie uma função eh_palindromo(texto) que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente).
# Requisitos:

# Ignore espaços
# Ignore maiúsculas/minúsculas
# Ignore pontuação (.,!?)
# Retorne True ou False

# Exemplo de uso:
# pythonprint(eh_palindromo("arara"))              # True
# print(eh_palindromo("Python"))             # False
# print(eh_palindromo("A man a plan a canal Panama"))  # True (sem espaços/pontuação)
# print(eh_palindromo("Socorram-me, subi no onibus em Marrocos"))  # True
# Dica: Use fatiamento de strings [::-1] para inverter.


def eh_palindromo(texto):


    texto = texto.lower()
    texto_limpo = ""


    for caractere in texto:
        if caractere.isalnum():
            texto_limpo += caractere

    return texto_limpo == texto_limpo[::-1]

print(eh_palindromo("Socorram-me, subi no onibus em Marrocos"))
print(eh_palindromo("ana"))
print(eh_palindromo("arara"))
print(eh_palindromo("vini"))
print("anaJulia"[::-1])
print("Python"[::-1])