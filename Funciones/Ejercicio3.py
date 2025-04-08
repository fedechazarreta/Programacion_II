def es_bisiesto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

def contar_bisiestos(ano_1, ano_2):
    if ano_2 <= ano_1:
        return "Error"
    return sum(1 for ano in range(ano_1, ano_2 + 1) if es_bisiesto(ano))

ano_1 = int(input("Ingrese el primer fecha: "))
ano_2 = int(input("Ingrese el segundo fecha: "))

resultado = contar_bisiestos(ano_1, ano_2)
print(f"El número de años bisiestos es: {resultado}")