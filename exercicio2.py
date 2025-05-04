num = int(input("Digite um numero inteiro positivo: "))
if num <0:
    print("INVALIDO")
else:
    soma = 0
    contador = 1
    while contador<= num:
        soma+=contador
        contador+=1
    print(f"A soma é {soma}")
