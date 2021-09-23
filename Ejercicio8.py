print("  Descuento    ")
print("[5 - 14] 35% \n"
      "[15- 19] 25% \n"
      "[20- 45] 10% \n"
      "[46- 65] 25% \n"
      "[66 en adelante] 25% " )
def Teatro():
    Valor = 0
    Descuento = 0
    Total = 0
total_personas = int(input("Ingrese la cantidad de personas"))
for i in range(total_personas):
    Valor = int(input("Ingrese el valor de la entrada: "))
    Edad = int(input("Ingrese la edad del cliente: "))
    if Edad< 5:
      print("Es menor de 5 años, no puede ingresar")  
    elif Edad >= 5 and Edad <=14:
        Descuento = (Valor * 0.35) / 100
        Total =  (Valor - Descuento)
        print(" Se realizo un descuento del 35% ")
        print(f'El total a pagar es: ${Total}')
    elif Edad >= 15 and Edad <=19:
        Descuento = (Valor * 0.25) / 100
        Total =  (Valor - Descuento)
        print("Se realizo un descuento del 25% ")
        print(f'El total a pagar es: ${Total}')
    elif Edad >= 20 and Edad <=45:
        Descuento = (Valor * 0.10) / 100
        Total =  (Valor - Descuento)
        print("Se realizo un descuento del 10% ")
        print(f'El total a pagar es: ${Total}')
    elif Edad >= 46 and Edad <=65:
        Descuento = (Valor * 0.25) / 100
        ValorFinal =  (Valor - Descuento)
        print("Se realizo un descuento del 25%")
        print(f'El total a pagar es: ${Total}')
    elif Edad >=66:
        Descuento = (Valor * 0.35) / 100
        ValorFinal =  (Valor - Descuento)
        print("Se realizo un descuento del 35% ")
        print(f'El total a pagar es: ${Total}')