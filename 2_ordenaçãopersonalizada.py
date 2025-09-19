import random
from collections import Counter

nomes = [
    "ADRIAN", "ANGELO", "ARTHUR", "CARLOS", "CHRISTOPHER", "DOUGLAS",
    "EMANUELLY", "EVERSON", "GABRIEL", "GUILHERME", "GUSTAVO A", "GUSTAVO P",
    "GUSTAVO", "ISABELLA", "JAMILE", "JOAO M", "JOÃO O", "JOAQUIM",
    "KALIKEY", "LUIS", "MARIA", "PEDRO A", "PEDRO G", "RAFAEL", "RAPHAEL",
    "RAPHAEL", "ROBERTO", "SOFIA", "STEPHANIE"
]
nomes[27] = "SEU_NOME"

random.shuffle(nomes)

colunas = 4
largura = max(len(nome) for nome in nomes) + 2

while len(nomes) % colunas != 0:
    nomes.append("")

print("\n===== LISTA DE NOMES EMBARALHADOS =====")
for i in range(0, len(nomes), colunas):
    linha = nomes[i:i+colunas]
    print("+" + "+".join("-" * largura for _ in linha) + "+")
    print("|" + "|".join(nome.center(largura) for nome in linha) + "|")
print("+" + "+".join("-" * largura for _ in linha) + "+")

print("\n===== ANÁLISE DE TEXTO =====")
texto = input("Digite um texto: ")

palavras = texto.split()

if len(palavras) > 0:
    print("\nQuantidade de palavras:", len(palavras))

    mais_longa = max(palavras, key=len)
    print("Palavra mais longa:", mais_longa)

    contagem = Counter(palavras)
    mais_comum, qtd = contagem.most_common(1)[0]
    print("Palavra que mais aparece:", mais_comum, f"({qtd} vezes)")
else:
    print("Nenhuma palavra digitada no texto.")
