num = int(input("Escreva um numero inteiro: "))
fim = 1
for fatorando in range(1,num+1):
    fim*=fatorando
print(f"o fatorial de {num} é: {fim}")
