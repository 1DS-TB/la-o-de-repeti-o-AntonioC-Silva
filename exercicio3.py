num = int(input("Escreva o numero da tabuada que você quer saber: "))
if num <0:
    print("INVALIDO")
else:
    for tabuada in range(1,11):
        print(f"{num} X {tabuada} = {num*tabuada}")