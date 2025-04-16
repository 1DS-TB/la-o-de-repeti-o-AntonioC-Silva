num = int(input("Escreva um numero: "))
vezes = ""
if num<0:
    print("invalido")
else:
    while True:
        for num in range(1, num+ 1):
            vezes = vezes+"*"
            print(vezes)
        break

