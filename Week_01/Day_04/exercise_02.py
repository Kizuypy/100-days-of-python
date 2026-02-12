# 💚 FÁCIL 2: Verificador de Palavra Única
# Contexto: Processamento de texto precisa identificar palavras únicas.
# Tarefa: Crie uma função tem_duplicatas(texto) que:

# Receba uma frase
# Separe em palavras (use .split())
# Use um set para verificar se há palavras repetidas
# Retorne True se houver duplicatas, False caso contrário

def tem_duplicatas(texto):
    palavras = texto.split()
    unicas = list(set(palavras))
    return unicas


print(tem_duplicatas("Olá everyone "))