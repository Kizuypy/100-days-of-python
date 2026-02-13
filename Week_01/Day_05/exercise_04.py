# ### 🧡 **Exercício 4: Conversor de Temperaturas com Map**

# **Descrição:**  
# Crie uma função lambda que converta Celsius para Fahrenheit. Use `map()` para converter uma lista de temperaturas.

# **Requisitos:**
# - Lambda: `(C × 9/5) + 32`
# - Lista de entrada: `[0, 10, 20, 30, 40]`
# - Use `map()` e converta para lista
# - Arredonde para 1 casa decimal

# **Saída esperada:**
# ```
# Celsius: [0, 10, 20, 30, 40]
# Fahrenheit: [32.0, 50.0, 68.0, 86.0, 104.0]
# ```

import math

lista = [0, 10, 20, 30, 40]
celsius_for_f = lambda c: math.ceil((c * 9/5 + 32) * 10) / 10

resultado = list(map(celsius_for_f, lista))
print(resultado)

