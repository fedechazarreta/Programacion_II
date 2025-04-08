def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def validar_division_por_cero(a, b):
   if b  == 0 :
       return("Error")


def division(a, b):
   if validar_division_por_cero(a, b) :
       return("Error")
   else:
       return a/b
   

def calculadora():
    print("1 = Suma, 2 = Resta, 3 = Multiplicacion, 4 = Division")
    opcion = input("Ingrese una opcion: ")
    
    a = int(input("Ingrese un numero a: "))
    b = int(input("Ingrese un numero b: "))
    
    if opcion == "1" :
        print("La suma es: ", suma(a,b))
    elif opcion == "2" :
        print("La resta es: ", resta(a,b))
    elif opcion == "3" :
        print("La multiplicacion es: ", multiplicacion(a,b))
    elif opcion == "4" :
        print("La division es: ", division(a,b)) 
        

calculadora()
        