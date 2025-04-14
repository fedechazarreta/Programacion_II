def saludar(nombre):
    print("Hola", nombre)

saludar("Seba")

def saludar1(nombre):
    return "Hola", nombre

saludo = saludar1("Fede")
print(saludo)