# NÍVEL MÉDIO 🟡
# EXERCÍCIO 5: Contador de Vogais
# Contexto: Análise de texto é comum em empresas (comentários, reviews, etc).
# Tarefa: Peça uma frase ao usuário e conte quantas vogais (a, e, i, o, u) tem na frase.
# Dicas:

# Use for letra in frase:
# Use if letra.lower() in 'aeiou':
# Crie um contador que começa em 0 e vai incrementando

frase = input("Digite uma frase: ")


contador_vogais = 0


for letra in frase:
    
    if letra.lower() in "aeiou":
        
        contador_vogais += 1

# 6. Mostrar o resultado
print("A frase tem", contador_vogais, "vogais.")