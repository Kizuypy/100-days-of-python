# NÍVEL MÉDIO 🟡
# EXERCÍCIO 9: Gerador de Relatório de Vendas
# Contexto: Empresas geram relatórios diários.
# Tarefa: Peça ao usuário para inserir vendas (valor) até digitar 'fim'.
# Depois mostre:

# Total de vendas
# Média de vendas
# Maior venda
# Menor venda
# Quantidade de vendas

# Dicas:

# Use while True e break quando digitar 'fim'
# Guarde as vendas numa lista
# Use funções built-in: sum(), len(), max(), min()
# Média = sum(vendas) / len(vendas)



vendas = []

while True:
    entrada = input('Insira o valor da venda (ou digite "fim"): ')

    if entrada.lower() == 'fim':
        break
    try:
        valor = float(entrada)
        vendas.append(valor)
    except ValueError:
        print('Digite um valor válido')

    if len(vendas) == 0:
        print('Nenhuma venda registrada.')
    else:
        print(f'Total de vendas: R${sum(vendas):.2f}')
        print(f'Média de vendas: R${(sum(vendas)/len(vendas)):.2f}')
        print(f'Maior venda: R${max(vendas):.2f}')
        print(f'Menor venda: R${min(vendas):.2f}')
        print(f'Quantidade de vendas: {len(vendas)}')
