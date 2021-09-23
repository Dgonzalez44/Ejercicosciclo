print ("  Valor vendido  "             "  Descuento  ")
print ("[Menor o = a 20 Millones]                         10%\n"
       "[Mayor de 20 Millones y menor de 40 Millones]     15%\n"
       "[Menor o = de 40 Millones y menor de 80 Millones] 20%\n"
       "[Mayor o = a 80 Millones y menor de 160 Millones] 25%\n"
       "[de 160 Millones en Adelante]                     30%")     

Comision = 0
Vendedores = int(input("Cantidad de vendedores a premiar: "))
for i in range(Vendedores):
    Nombre = str(input("Ingrese el nombre del vendedor"))
    Ventas = int(input(f"Ingrese las ventas de {Nombre} es: "))
    if (Ventas <= 20000000):
        Comision += Ventas * 0.10
    print(f"La comision de {Nombre} es de {Comision}")
    if (Ventas > 20000000 and Ventas < 40000000):
        Comision += Ventas * 0.15
    print(f"La comision de {Nombre} es de {Comision}")
    if(Ventas >= 40000000 and Ventas < 80000000):
        Comision += Ventas * 0.20
        print(f"La comision del {Nombre} es de {Comision}")

    elif(Ventas >= 80000000 and Ventas < 160000000):
        Comision += Ventas * 0.25
        print(f"La comision del {Nombre} es de {Comision}")

    elif(Ventas >= 160000000):
        Comision += Ventas * 0.30
        print(f"La comision del {Nombre} es de {Comision}")

    else:
        print("No tiene comisiones y esta despedido")



