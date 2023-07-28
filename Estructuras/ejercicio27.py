cantidad_puntos = int(input("Ingrese la cantidad de puntos: "))

puntos_primer_cuadrante = 0
puntos_segundo_cuadrante = 0
puntos_tercer_cuadrante = 0
puntos_cuarto_cuadrante = 0

for i in range(cantidad_puntos):
    print(f"\nPunto {i+1}:")
    x = float(input("Ingrese la coordenada x: "))
    y = float(input("Ingrese la coordenada y: "))

    if x > 0 and y > 0:
        puntos_primer_cuadrante += 1
    elif x < 0 and y > 0:
        puntos_segundo_cuadrante += 1
    elif x < 0 and y < 0:
        puntos_tercer_cuadrante += 1
    elif x > 0 and y < 0:
        puntos_cuarto_cuadrante += 1

print("\nResultados:")
print(f"Cantidad de puntos en el primer cuadrante: {puntos_primer_cuadrante}")
print(f"Cantidad de puntos en el segundo cuadrante: {puntos_segundo_cuadrante}")
print(f"Cantidad de puntos en el tercer cuadrante: {puntos_tercer_cuadrante}")
print(f"Cantidad de puntos en el cuarto cuadrante: {puntos_cuarto_cuadrante}")
