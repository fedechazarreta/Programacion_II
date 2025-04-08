def validar_nota(iteracion):
    
            nota = float(input(f"Ingrese la nota {iteracion} (entre 0 y 10): "))
            if 0 <= nota <= 10:
                return nota
            print("Error: La nota debe estar entre 0 y 10.")
        
def main():
    suma_notas = 0
    for i in range(1, 5):
        suma_notas += validar_nota(i)
    promedio = suma_notas / 4
    print(f"El promedio de las cuatro notas es: {promedio:.2f}")

main()
