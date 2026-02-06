# NÍVEL FÁCIL 💚
# EXERCÍCIO 1: Cadastro de Funcionário
# Contexto: Toda empresa precisa cadastrar funcionários no sistema.
# Tarefa: Crie um programa que peça:

# Nome do funcionário
# Idade
# Salário

# Depois mostre uma mensagem formatada:
# "Funcionário [NOME], [IDADE] anos, salário R$ [SALÁRIO]"



nome = input('Digite seu nome: ')
try:
    idade = int(input('Digite sua idade: '))
    salario = float(input('Digite seu salário: '))
except ValueError:
    print('Formatação Inválida, somente números! ')
    exit()


print('-' * 40)
print('Dados do funcionário:')
print('-' * 40)


print()
print(f'Seu nome é: {nome} \n'
f'Sua idade é: {idade} anos\n'
f'e seu salário é de R${salario:.2f}')





