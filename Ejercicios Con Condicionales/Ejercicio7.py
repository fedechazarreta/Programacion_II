numero_secreto = 10
numero_usuario = int(input("Adivinar numero entre 1 y 10: "))

if numero_secreto == numero_usuario:
    print("Felicitaciones adivinaste el numero")
else :
    print(f"Incorrecto, el numero es {numero_secreto}")