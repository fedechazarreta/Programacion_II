def añobisiesto(a):
    if a % 4 == 0 and a % 100 !=0 :
        print("True")
    else:
        print("False")

añobisiesto(a=int(input("Ingrese un anio: ")))