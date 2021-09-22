def animales(valores, nombre):
    A1 = 0
    A2 = 0
    A3 = 0
    for valor in range(valores):
        Edad = int(input(f"Ingrese la edad del animal #{(valor+1)}: "))
        if Edad >= 0 and Edad <= 1:
            A1 = A1+1
        elif Edad > 1 and Edad <= 3:
            A2 = A2+1
        elif Edad > 3:
            A3 = A3+1
    print(f"Porcentaje de {nombre} de 0 a 1 año: {(A1/valores)*100}")
    print(f"Porcentaje de {nombre} mas de 1 y menor de 3 años: "
          f"{(A2/valores)*100}")
    print(f"Porcentaje de {nombre} mayores de 3 años: {(A3/valores)*100}")


print("     ZOOLOGICO     ")
valores = int(input("Que animal desea verificar\n"
                    "1. Elefante\n2. Jirafa\n3. Chimpanse"))
if valores == 1:
    valores = 20
    nombre_animal = 'Elefantes'
    animales(valores, nombre_animal)
elif valores == 2:
    valores = 15
    nombre_animal = 'Jirafas'
    animales(valores, nombre_animal)
elif valores == 3:
    valores = 40
    nombre_animal = 'Chimpanses'
    animales(valores, nombre_animal)
