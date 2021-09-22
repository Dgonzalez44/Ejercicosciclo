

def acumular ():
    acumulador = int(0)
    sexo = input("ingrese el sexo de la persona. \nMujer \nHombre \nGrupo de alumnos")
    if sexo == 'mujer' or sexo == 'Mujer':
        num = int(input('cuantos datos va ingresar: '))
        for x in range(num):
            edad = int(input("Ingresar la edad"))
            acumulador = acumulador + edad
            print(" Promedio del grupo es:", str(acumulador / num))
    
acumular()