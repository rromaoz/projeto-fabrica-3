# 🛒 Comparador de Preços

Projeto minimalista em **Python** para decidir **onde comprar mais barato** o *mesmo produto* em **3 supermercados**.  
Sem limpezas de string nem formatação de moeda: **digite os preços como `float` usando ponto** (ex.: `27.90`).

---

## 📝 Enunciado
Você fará uma pesquisa de preços do **mesmo produto** (ex.: *Arroz 5kg*) em **três supermercados** e decidirá **onde comprar**.  
O programa deve:
1. Perguntar o **nome do produto**.
2. Perguntar o **nome** e o **preço** (em `float`) do produto em **3 supermercados**.
3. Informar **qual(is)** supermercado(s) tem/têm o **menor preço** e exibir o valor.

> Exemplo de uso
```
Produto (ex.: Arroz 5kg): Arroz 5kg
Nome do supermercado 1: Mercado Central
Preço no Mercado Central (use ponto, ex.: 27.90): 27.90
Nome do supermercado 2: Super Bom
Preço no Super Bom (use ponto, ex.: 27.90): 29.50
Nome do supermercado 3: Preço Justo
Preço no Preço Justo (use ponto, ex.: 27.90): 27.90

=== Resultado ===
Produto: Arroz 5kg
Mais barato em: Mercado Central, Preço Justo
Preço: 27.90
```

---

## 💻 Como executar

Pré‑requisito: **Python 3.8+**

1) Clone este repositório ou baixe os arquivos.
```bash
git clone https://github.com/seu-usuario/projeto-fabrica-3.git
cd projeto-fabrica-3
```

2) Rode o programa:
```bash
python comparador.py
```

3) **Importante:** digite os preços com **ponto** (`.`) como separador decimal (ex.: `12.50`).

> Dica (Windows): se `python` não funcionar, tente `py comparador.py`.

---

## 🧪 (Opcional) Rodando testes
Sem dependências externas. Use o `unittest` padrão:
```bash
python -m unittest
```

---

## 🎯 Conceitos trabalhados
- Entrada de dados com `input()`  
- Conversão para `float`  
- Lógica de **mínimo** e **empate** simples  
- Saída formatada com `print()`

---

## 🚀 Extensões sugeridas
- **Empate + frete**: adicionar custo de deslocamento e reordenar.
- **Descontos**: cupom, clube de vantagens, taxa de entrega.
- **CSV**: importar/exportar pesquisas de preço.
- **Múltiplos produtos**: somar o carrinho por supermercado.
- Interface gráfica simples com **Tkinter** ou **Streamlit**.

---

## 📂 Estrutura do projeto
```
projeto-fabrica-3/
├─ comparador.py
├─ README.md
├─ tests/
│  └─ test_comparador.py
├─ .gitignore
└─ LICENSE
```

---

## 📝 Licença
Este projeto está sob licença **MIT** — use, compartilhe e adapte. ✨
