carrinho = []



while True:

    
    while True:
        nome_produto = input("Digite o nome do produto: ").strip()
        if not nome_produto:
            print("❌ Nome não pode ser vazio!")
        else:
            break

    
    while True:
        try:
            valor_produto = float(input("Digite o valor do produto: "))
            if valor_produto <= 0:
                print("❌ O valor deve ser maior que zero!")
                continue
            break
        except ValueError:
            print("❌ Digite um número válido!")

    
    while True:
        try:
            quantidade_produto = int(input("Digite a quantidade: "))
            if quantidade_produto < 1:
                print("❌ A quantidade deve ser pelo menos 1!")
                continue
            break
        except ValueError:
            print("❌ Digite um número inteiro válido!")

    
    carrinho.append([nome_produto, valor_produto, quantidade_produto])
    print("✅ Produto adicionado com sucesso!")

    continuar = input("Deseja adicionar mais produtos? (s/n): ").strip().lower()
    if continuar != "s":
        break




print("\n===== PRODUTOS NO CARRINHO =====")

total_compra = 0

for produto in carrinho:
    nome = produto[0]
    valor = produto[1]
    quantidade = produto[2]

    subtotal = valor * quantidade
    total_compra += subtotal

    print(f"Produto: {nome}")
    print(f"Valor unitário: R$ {valor:.2f}")
    print(f"Quantidade: {quantidade}")
    print(f"Subtotal: R$ {subtotal:.2f}")
    print("-" * 30)


print(f"\nTotal da compra: R$ {total_compra:.2f}")



if total_compra <= 100:
    desconto_progressivo = 0
elif total_compra <= 500:
    desconto_progressivo = total_compra * 0.05
elif total_compra <= 1000:
    desconto_progressivo = total_compra * 0.10
else:
    desconto_progressivo = total_compra * 0.15

valor_com_desconto = total_compra - desconto_progressivo

print(f"Desconto progressivo: R$ {desconto_progressivo:.2f}")




cupom = input("\nDigite o cupom (PROMO10 ou PROMO20) ou pressione Enter para pular: ").strip().upper()

desconto_cupom = 0

if cupom == "PROMO10":
    desconto_cupom = valor_com_desconto * 0.10
elif cupom == "PROMO20":
    desconto_cupom = valor_com_desconto * 0.20
elif cupom != "":
    print("⚠️ Cupom inválido! Desconsiderando...")

valor_final = valor_com_desconto - desconto_cupom




print("\n===== RESUMO FINAL =====")
print(f"Total da compra: R$ {total_compra:.2f}")
print(f"Desconto progressivo: R$ {desconto_progressivo:.2f}")
print(f"Desconto cupom: R$ {desconto_cupom:.2f}")
print(f"Valor final a pagar: R$ {valor_final:.2f}")

