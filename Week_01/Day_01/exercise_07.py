# NÍVEL DIFÍCIL 🔴
# EXERCÍCIO 7: Validador de CPF
# Contexto: Muitas empresas precisam validar CPF (você já viu no curso!).
# Tarefa: Crie um programa que:

# Peça um CPF (apenas números)
# Valide se tem 11 dígitos
# Calcule os 2 dígitos verificadores
# Diga se o CPF é válido ou não

# Dicas:

# Revise as aulas 99-103! (É do meu cursinho de python :D)
# Use slice para pegar os 9 primeiros dígitos
# Use enumerate e for para multiplicar pelos pesos
# Lembre: resto da divisão por 11, se for > 9, dígito é 0


cpf = input('Digite seu CPF (apenas números): ').strip()


if len(cpf) != 11 or not cpf.isdigit():
    print('CPF inválido: precisa ter 11 dígitos numéricos.')


elif cpf == cpf[0] * 11:
    print('CPF inválido: números sequenciais.')

else:
    print('CPF com formato válido. Continuando validação...')

    soma = 0
    nove_digitos = cpf[:9]

    for i, numero in enumerate(nove_digitos):
        soma += int(numero) * (10 - i)

    resto = soma % 11
    digito = 11 - resto

    if digito > 9:
        digito = 0

    soma = 0
    if digito == int(cpf[9]):
        print('Primeiro dígito válido.')

    soma = 0
    dez_digitos = cpf[:10]

    for i, numero in enumerate(dez_digitos):
        soma += int(numero) * (11 - i)

    resto = soma % 11
    segundo_digito = 11 - resto

    if segundo_digito > 9:
        segundo_digito = 0

    if segundo_digito == int(cpf[10]):
        print('CPF VÁLIDO!')
    else:
        print('CPF INVÁLIDO!')

