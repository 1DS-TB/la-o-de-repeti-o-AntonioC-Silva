inicio = int(input("digite o inicio: "))
fim = int(input("digite o fim: "))
print("numeros de kaprekar encontrados:")
for k in range(inicio, fim + 1):
    quadrado = str(k ** 2)
    tamanho = len(str(k))
    direita = quadrado[-tamanho:]
    esquerda = quadrado[:-tamanho]
    if esquerda == "":
        esquerda = "0"
    soma = int(esquerda) + int(direita)
    if soma == k and int(direita) != 0:
        print(k)
