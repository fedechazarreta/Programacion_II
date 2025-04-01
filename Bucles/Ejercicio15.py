contador = 0
nueva_lista = []

lista = [4343, 3434,343,-123,-1235,-15, 2, 5]
for num in lista:
        if num >= 0:
            nueva_lista.append(num)
while contador < len(nueva_lista):
        contador += 1
print(contador)