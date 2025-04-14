def contar_letra(texto):
    contador=0
    for i in texto:
     if i.isalpha():
         contador +=1
         print(contador)
         
letra=contar_letra("Morena Aguirre")
print(letra)