# 🟢 EXERCÍCIOS FÁCEIS
# Exercício 1: Conversor de Temperatura
# Descrição:
# Crie uma função converter_temperatura(valor, escala_origem, escala_destino) que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
# Requisitos:

# Suporte para 'C', 'F' e 'K' (case-insensitive)
# Fórmulas:

# C para F: (C × 9/5) + 32
# C para K: C + 273.15
# F para C: (F - 32) × 5/9


# Retorne o valor convertido arredondado para 2 casas decimais
# Se as escalas forem iguais, retorne o valor original

# Exemplo de uso:
# pythonprint(converter_temperatura(0, 'C', 'F'))      # 32.0
# print(converter_temperatura(32, 'F', 'C'))     # 0.0
# print(converter_temperatura(25, 'C', 'K'))     # 298.15
# Dica: Use condicionais compostas com and para verificar as escalas.



def converter_temperatura(valor, escala_origem, escala_destino):



    escala_origem = escala_origem.upper()
    escala_destino = escala_destino.upper()

    if escala_origem == escala_destino:
        return valor

    # CONVERSÕES DE CELSIUS
    if escala_origem == 'C' and escala_destino == 'F':
        resultado = (valor * 9 / 5) + 32
        return round(resultado, 2)

    if escala_origem == 'C' and escala_destino == 'K':
        resultado = (valor - 32) * 5 / 9
        return round(resultado, 2)

    # CONVERSÕES DE FAHRENHEIT

    if escala_origem == 'F' and escala_destino == 'C':
        resultado = (valor * 9 / 5) + 32
        return round(resultado, 2)

    if escala_origem == 'F'and escala_destino == 'K':
        celsius = (valor - 32) * 5/9
        resultado = celsius + 273.15
        return round(resultado, 2)

    if escala_origem == 'K' and escala_destino == 'C':
        resultado = valor - 273.15
        return round(resultado,2)

    if escala_origem == 'K' and escala_destino == 'F':
        celsius = valor - 273.15
        resultado = (celsius * 9 / 5) + 32
        return round(resultado, 2)


print("=== TESTES DO CONVERSOR ===")

print(f"0°C para F: {converter_temperatura(0, 'C', 'F')}°F") 
print(f"32°F para C: {converter_temperatura(32, 'F', 'C')}°C") 