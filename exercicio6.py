num = int(input("Escreva um numero: "))
lista = []
somar = 0
contador = 1
if num <0:
    print("INVALIDO")
else:
    if num<0:
        print("invalido")
    else:
        while contador<=num:
            somar+=1
            contador+=1
            f = contador+contador
            lista.append(f)
    print(lista)