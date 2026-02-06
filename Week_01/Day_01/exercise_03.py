# NÍVEL FÁCIL 💚
# EXERCÍCIO 3: Calculadora de Desconto
# Contexto: Lojas precisam calcular descontos para clientes.
# Tarefa: Peça:

# Valor do produto
# Percentual de desconto

# Calcule e mostre:

# Valor do desconto
# Valor final do produto

# Dicas:

# Desconto = valor * (percentual / 100)
# Valor final = valor - desconto
# Use f-strings para formatar com 2 casas decimais: f'{valor:.2f}'

print('-' * 40)
print('Calculadora de Desconto: ')


valor_produto = float(input('Digite o valor do produto: '))

percentual = float(input('Digite o valor do desconto: '))

desconto =  valor_produto * (percentual / 100)

valor_final = valor_produto - desconto


print('-' * 40)
print('Informações do produto: ')
print('-' * 40)
print()
print(f'O valor do produto é R${valor_produto:.2f}\n')
print(f'O valor do desconto é {desconto:.2f}\n')
print(f'O valor final do produto com desconto é R${valor_final:.2f}')


