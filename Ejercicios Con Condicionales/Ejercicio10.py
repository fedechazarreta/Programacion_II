categoriaABC = input("Ingrese categoria A/B/C: ")
hora =  int(input("Ingrese cuantas horas trabajo: ")) 
dias =  int(input("Ingrese cuantos dias trabajo: ")) 

if categoriaABC == "A":
   Platapordia = 100
   PLataporhora = 100
   Maxdias = 30
if categoriaABC == "B":
    Platapordia = 100
    PLataporhora = 80
    Maxdias = 24

if categoriaABC == "C":
   Platapordia = 100
   PLataporhora = 100
   Maxdias = 24

else :
    print("Categoria incorrecta: ")
    
promedio_hora = dias/hora
dias_validos = dias <= Maxdias

if promedio_hora >= 4 :
    plata_fijo = Platapordia * dias_validos
else :
    plata_fijo = 0
    
plata_variable = PLataporhora * hora

total = plata_variable + plata_fijo
print(total)