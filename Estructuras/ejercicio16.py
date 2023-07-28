n = int(input("Ingrese la cantidad de alturas a ingresar: "))

alturas = []
for i in range(n):
    altura = float(input("Ingrese la altura de la persona: "))
    alturas.append(altura)

promedio = sum(alturas) / n

print("La altura promedio de las personas es:", promedio)
