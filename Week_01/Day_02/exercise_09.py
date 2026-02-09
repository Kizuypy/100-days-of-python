# NÍVEL MÉDIO 🟡
# EXERCÍCIO 9: Sistema de Relatório de Vendas por Vendedor
# Contexto: Empresas geram relatórios diários de desempenho.
# Tarefa: Crie um programa que:

# 1. Registre vendas de vários vendedores:
#    - Nome do vendedor
#    - Valor da venda (deve ser > 0)
#    - Armazene: [nome_vendedor, valor]
#    - Continue perguntando até digitar 'fim' no nome

# 2. Mostre o relatório geral:
#    - Total de vendas (soma)
#    - Média de vendas
#    - Maior venda (valor + nome do vendedor)
#    - Menor venda (valor + nome do vendedor)
#    - Quantidade de vendas registradas

# 3. Mostre ranking de vendedores:
#    - Liste cada vendedor único
#    - Mostre quantas vendas cada um fez
#    - Mostre o total vendido por cada um
#    - Exemplo: "João: 3 vendas - R$ 1.500,00"

# DICA: Para agrupar por vendedor, percorra a lista e conte/some




from Week_01.Day_02.exercise_03 import quantidade


vendas = []
ranking = {}
maior_venda = vendas[0]
menor_venda = vendas[0]

while True:
    print('\n Escolha uma das opções a baixo: ')
    opcao = input('1 - Registrar Venda\n'
    '2 - Relatório Geral\n'
    '3 - Ranking Vendedores\n'
    '4 - Sair do programa: ')

    if not opcao:
        print('Opção não pode estar vazia!')
        continue

    elif opcao == "1":
        while True:
            nome_vendedor = input("Digite o nome do vendedor (ou 'fim' para voltar): ").strip()
            if not nome_vendedor:
                print("O nome do vendedor não pode estar vazio!")
            elif nome_vendedor.lower() == "fim":
                break
            else:
                while True:
                    try:
                        valor_venda = float(input("Digite o valor da venda: "))
                        if valor_venda <= 0:
                            print("Valor da venda deve ser maior que zero!")
                            continue
                        break
                    except ValueError:
                        print("Digite um número válido!")
                
                vendas.append([nome_vendedor, valor_venda])
                print(f"Venda registrada: {nome_vendedor} - R$ {valor_venda:.2f}")
                break  
    elif opcao == "2":
        if len(vendas) == 0:
            print("Nenhuma venda registrada!")
        else:
            sub_total = 0
            maior_venda = vendas[0]
            menor_venda = vendas[0]

            print("=== Relatório Geral ===")
            for i, venda in enumerate(vendas, start=1):
                nome, valor = venda
                sub_total += valor

                if valor > maior_venda[1]:
                    maior_venda = venda
                if valor < menor_venda[1]:
                    menor_venda = venda

                print(f"{i}. {nome} - R$ {valor:.2f}")

            media_vendas = sub_total / len(vendas)

            print(f"\nTotal de Vendas: R$ {sub_total:.2f}")
            print(f"Média de Vendas: R$ {media_vendas:.2f}")
            print(f"Vendas registradas: {len(vendas)}")
            print(f"Maior venda: {maior_venda[0]} - R$ {maior_venda[1]:.2f}")
            print(f"Menor venda: {menor_venda[0]} - R$ {menor_venda[1]:.2f}")

    elif opcao == "3":
        if len(vendas) == 0:
            print("Nenhuma venda registrada!")
        else:
            ranking = {}  
            for venda in vendas:
                nome, valor = venda
                if nome not in ranking:
                    ranking[nome] = {"quantidade": 0, "total": 0}
                ranking[nome]["quantidade"] += 1
                ranking[nome]["total"] += valor

            print("=== Ranking de Vendedores ===")
            for vendedor, info in ranking.items():
                qtd = info["quantidade"]
                total = info["total"]
                print(f"{vendedor}: {qtd} venda(s) - R$ {total:.2f}")

    elif opcao == "4":
        print("Saindo do programa. Até mais!")
        break

    else:
        print("Opção inválida! Digite 1, 2, 3 ou 4.")