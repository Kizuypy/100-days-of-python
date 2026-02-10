# 🔴 **EXERCÍCIOS DIFÍCEIS**

### **Exercício 5: Validador de CPF Completo**

# **Descrição:**
# Crie uma função `validar_cpf(cpf)` que valide um CPF brasileiro completo.

# **Requisitos:**
# - Aceite CPF com ou sem formatação (123.456.789-10 ou 12345678910)
# - Remova caracteres não numéricos
# - Verifique se tem 11 dígitos
# - Valide os dois dígitos verificadores usando o algoritmo oficial
# - CPFs com todos os dígitos iguais são inválidos (111.111.111-11)
# - Retorne True se válido, False caso contrário

# **Algoritmo dos dígitos verificadores:**
# ```
# Primeiro dígito:
# - Multiplique os 9 primeiros dígitos pela sequência 10, 9, 8, 7, 6, 5, 4, 3, 2
# - Some os resultados
# - Multiplique por 10 e divida por 11
# - O resto da divisão é o primeiro dígito (se for 10, considere 0)

# Segundo dígito:
# - Multiplique os 10 primeiros dígitos pela sequência 11, 10, 9, 8, 7, 6, 5, 4, 3, 2
# - Mesmo processo

def validar_cpf(cpf):

    cpf_limpo = ""

    for caractere in cpf:
        if caractere.isdigit():
            cpf_limpo += caractere

    if len(cpf_limpo) != 11:
        return False

    if cpf_limpo == cpf_limpo[0] * 11:
        return False

    soma = 0
    peso = 10

    for i in range(9):
        soma += int(cpf_limpo[i]) * peso
        peso -= 1

    primeiro_digito = (soma * 10) % 11

    if primeiro_digito == 10:
        primeiro_digito = 0

    
    soma = 0 
    peso = 11

    for i in range(10):
        soma += int(cpf_limpo[i]) * peso
        peso -= 1

    segundo_digito = (soma * 10) % 11

    if segundo_digito == 10:
        segundo_digito = 0

    if (int(cpf_limpo[9]) == primeiro_digito and
        int(cpf_limpo[10]) == segundo_digito):
        return True

    return False