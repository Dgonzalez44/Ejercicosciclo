salir = "y"
lista = [0, 0, 0, 0, 0]
color = 1
placa = 0


def registro(placa):
    # Sacar el ultimo digito del string
    placa = int(placa[-1])
    print(placa)
    if placa == 1 or placa == 2:
        pos = 0
    elif placa == 3 or placa == 4:
        pos = 1
    elif placa == 5 or placa == 6:
        pos = 2
    elif placa == 7 or placa == 8:
        pos = 3
    elif placa == 9 or placa == 0:
        pos = 4
    lista[pos] += color


def mostrarplaca():
    print(f"Cantidad carro amarillo {lista[0]}")
    print(f"Cantidad carro rosa: {lista[1]}")
    print(f"Cantidad carro roja: {lista[2]}")
    print(f"Cantidad carro verde: {lista[3]}")
    print(f"Cantidad carro azul: {lista[4]}")


print("------------ SOFTWARE CONTABILIZADOR DE CARROS -------------")
while salir == "y" or salir == "Y":
    placa = input("Digite el numero de la placa: ")
    registro(placa)
    salir = input("Continuar: Y/N ")
mostrarplaca()
