nomes = []
print("Digite 10 nomes:")

contador = 0
while contador < 10:
    nome = input("Digite o nome {}: ".format(contador + 1))

    if not nome.replace(" ", "").isalpha():
        print("Nome inválido! Use apenas letras e espaços.")
        break

    nomes.append(nome)
    contador += 1

if len(nomes) == 10:
    nomes.sort()

    print("\nQuantidade de letras (sem contar espaços):")
    for nome in nomes:
        letras = nome.replace(" ", "")
        print(nome, "tem", len(letras), "letras.")

    =
    print("\nAgora digite um texto para análise:")
    texto = input("Texto: ")

    palavras = texto.split()

    if len(palavras) > 0:
       
        print("\nQuantidade de palavras:", len(palavras))

        mais_longa = max(palavras, key=len)
        print("Palavra mais longa:", mais_longa)
      
        from collections import Counter
        contagem = Counter(palavras)
        mais_comum, qtd = contagem.most_common(1)[0]
        print("Palavra que mais aparece:", mais_comum, f"({qtd} vezes)")
    else:
        print("Nenhuma palavra digitada no texto.")
