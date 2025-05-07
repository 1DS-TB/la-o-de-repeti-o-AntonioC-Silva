num = int(input("digite a quantidade de termos da serie harmonica: "))
soma = 0
contador = 1
if num <0:
    print("INVALIDO")
else:
    while contador <= num:
        soma += 1 / contador
        contador += 1
    print(f"a soma da serie harmonica é: {soma:.2f}")
