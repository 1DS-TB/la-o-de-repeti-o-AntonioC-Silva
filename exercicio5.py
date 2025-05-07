num = int(input("Escreva um numero: "))
<<<<<<< HEAD
if num<2:
    print("O numero não é primo")
elif num == 2:
    print("O numero é primo")
for divisao in range(2, num):
    if num % divisao == 0:
        print(f"O numero {num} não é primo.")
        break
    else:
        print(f"O numero {num} é primo.")
        break
=======
if num <0:
    print("INVALIDO")
else:
    if num<2:
        print(" O numero não é primo")
    elif num == 2:
        print("O numero é primo")
    for divisao in range(2, num):
        if num % divisao == 0:
            print(f"O numero {num} não é primo.")
            break
        else:
            print(f"O numero {num} é primo.")
            break
>>>>>>> 1254591b2886264716064d81cacaa1863332e4b9
