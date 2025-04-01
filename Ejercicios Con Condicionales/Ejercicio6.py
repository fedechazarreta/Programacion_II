anio = int(input("Ingresar anio para determinar si es o no bisiesto:"))

if anio % 4 == 0 and anio % 100 !=0 :
    print("El anio es bisiesto")
else :
    print("El anio no es bisiesto")