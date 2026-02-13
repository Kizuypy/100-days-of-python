# 📌 Day 05 - Exercícios de Python (Lambda e List Comprehension)

## Resumo do dia

Hoje pratiquei **lambda, map, filter e list comprehension** — formas mais compactas e "pythônicas" de trabalhar com listas e transformações de dados. Foi um dia tranquilo comparado aos anteriores.

---

## Exercícios Realizados

| Nº | Exercício | Contexto | Nível | Conceitos Praticados |
|----|-----------|----------|-------|---------------------|
| 1 | Dobrar Números com Lambda | Transformação de dados | Fácil 💚 | Lambda, map(), conversão para lista |
| 2 | Filtrar Números Pares | Filtragem de dados | Fácil 💚 | Lambda, filter(), operador módulo |
| 3 | List Comprehension com Condição | Criação de listas | Médio 🧡 | List comprehension, condicionais, potência |
| 4 | Conversor de Temperaturas | Conversão científica | Médio 🧡 | Lambda, map(), math.ceil(), arredondamento |
| 5 | Filtrar Nomes Curtos | Processamento de strings | Médio 🧡 | Lambda, filter(), len() |

---

## Detalhes dos Exercícios

### 💚 Exercício 1: Dobrar Números com Lambda
Criar função lambda que dobra números e aplicar em lista usando `map()`.
- **Input**: `[1, 2, 3, 4, 5]`
- **Output**: `[2, 4, 6, 8, 10]`
- **Aprendi:** Lambda é compacto e `map()` substitui loops

### 💚 Exercício 2: Filtrar Números Pares
Usar `filter()` com lambda para pegar apenas números pares.
- **Input**: `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`
- **Output**: `[2, 4, 6, 8, 10]`
- **Aprendi:** `filter()` precisa de função que retorne True/False

### 🧡 Exercício 3: List Comprehension com Condição
Criar lista com quadrado de números ímpares usando list comprehension.
- **Input**: números de 1 a 10
- **Output**: `[1, 9, 25, 49, 81]`
- **Aprendi:** List comprehension com `if` é muito poderoso

### 🧡 Exercício 4: Conversor de Temperaturas
Lambda que converte Celsius → Fahrenheit usando `map()`.
- **Input**: `[0, 10, 20, 30, 40]`
- **Output**: `[32.0, 50.0, 68.0, 86.0, 104.0]`
- **Aprendi:** `math.ceil()` pra arredondar e controlar casas decimais

### 🧡 Exercício 5: Filtrar Nomes Curtos
Filtrar nomes com 5 letras ou menos usando `filter()`.
- **Input**: `["Ana", "João", "Maria", "Pedro", "Fernanda", "Carlos", "Bia"]`
- **Output**: `['Ana', 'João', 'Maria', 'Pedro', 'Bia']`
- **Aprendi:** `len()` funciona em strings

---

## Conteúdo estudado (curso)

Assisti às aulas sobre:
- Introdução à função lambda + list.sort e sorted
- Funções lambda complexas (para entendimento)
- Empacotamento e desempacotamento de dicionários + *args e **kwargs
- Introdução à List comprehension em Python
- Mapeamento de dados em list comprehension (map)
- Filtro de dados em list comprehension (filter)

---

## Notas do dia

📖 [Ver notas detalhadas](NOTES.md)

---

## Progresso Geral

✅ Day 01 concluído  
✅ Day 02 concluído  
✅ Day 03 concluído  
✅ Day 04 concluído  
✅ Day 05 concluído  
⬜ Day 06  
⬜ Day 07  

---

💡 **Meu objetivo**: aprender Python de forma prática e consistente, registrando cada exercício e anotação.