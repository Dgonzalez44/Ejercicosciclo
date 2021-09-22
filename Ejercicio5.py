Numeros=int(input("Cantidad que desea en el conjunto: "))
num = []
for i in range(Numeros):
    num.append(int(input("Digite un numero: ")))
minimo = num[0]
for i in range(Numeros):
    if num[i] < minimo:
        minimo = num[i]
print("\n")
print("El número más pequeño es: " + str(minimo))

    