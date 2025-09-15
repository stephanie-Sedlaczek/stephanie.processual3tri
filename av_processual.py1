import random
import string

nome = "SEU_NOME"
tamanho_total = 20

if len(nome) > tamanho_total:
    print("Erro: o nome é maior que o tamanho total da senha!")
else:
    tamanho_restante = tamanho_total - len(nome)
    metade = tamanho_restante // 2

    caracteres = string.ascii_letters + string.digits + string.punctuation

    antes = ''.join(random.choice(caracteres) for _ in range(metade))
    depois = ''.join(random.choice(caracteres) for _ in range(tamanho_restante - metade))

    senha = antes + nome + depois

    print("Senha gerada:", senha)
