def contar_vocales(palabra):
    vocales = "aeiuoAEIUO"
    contador = 0

    for i in palabra :
        if i in vocales:
            contador += 1
            
    print("vocales", contador)

palabraa=contar_vocales("Morena")
print(palabraa)