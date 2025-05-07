num = int(input("Escreva o numero da tabuada que você quer saber: "))
for tabuada in range(1,11):
    multiplicacao = num*tabuada
    print(f"{num} x {tabuada} = {multiplicacao}")