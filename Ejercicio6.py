def peso():
    peso = 0
UltimoPeso = 0
AcumuladorPeso = 0
DiferenciaPeso = 0
PromedioPeso = 0
U_peso = int(input("Ingrese su ultimo peso "))
for x in range(10):
    peso = int(input("Ingrese su  peso "))
    AcumuladorPeso = AcumuladorPeso + 1
PromedioPeso = AcumuladorPeso / 10
DiferenciaPeso = PromedioPeso - U_peso
if DiferenciaPeso > 0:
   print(f"SUBIO {DiferenciaPeso}") 
elif DiferenciaPeso < 0:
   print(f"BAJO {DiferenciaPeso}")