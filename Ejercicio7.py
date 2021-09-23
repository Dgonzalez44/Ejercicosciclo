def precio():
    cantidad=0  
    valor=0
Cantidad = int(input("Ingrese la cantidad que va a comprar del articulo"))
for i in range(Cantidad):
    Precio = int(input("Ingrese el valor del articulo tomado"))
Total = Precio * Cantidad
print(f"el precio total es ${Total}")
 