def Horas():
    
    numobreros = int(input('Cuantos obreros trabajan en la empresa: '))
    for valor in range(numobreros):
        Hora = int(input(f"Ingrese la Cantidad de horas trabajadas #{(valor)}:"))
        if Hora <= 40 :
            total1 = Hora * 20
            print(f"El salario semanal es: {total1}")
        elif Hora > 40 :
            resta = Hora - 40
            total2 = ((40 * 20) + (resta * 25))
            print(f"El salario semanal es: {total2}")

Horas()
