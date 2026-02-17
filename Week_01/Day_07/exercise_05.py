# ❤️ Exercício 5: Generator de Leitura de Arquivo Linha por Linha
# Descrição:
# Crie um generator ler_linhas(nome_arquivo) que leia um arquivo linha por linha sem carregar tudo na memória.
# Requisitos:

# Use yield para retornar cada linha
# Use try/except para tratar FileNotFoundError
# Use finally para fechar o arquivo
# Se erro, não gere nenhuma linha

def ler_linhas(nome_arquivo):
    arquivo = None
    try:
        arquivo = open(nome_arquivo, "r", encoding="utf-8")
        
        for linha in arquivo:
            yield linha
    
    except FileNotFoundError:
        print("Erro: arquivo não encontrado.")
    
    finally:
        if arquivo is not None:
            arquivo.close()
