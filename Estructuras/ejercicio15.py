n=1
notas_mayores_siete = 0
notas_menores_siete = 0

while n<=10:
    nota = float(input("Ingrese la nota del alumno: "))
    if nota >= 7:
        notas_mayores_siete += 1
    else:
        notas_menores_siete += 1
n=n+1

print("Cantidad de alumnos con notas mayores o iguales a 7:", notas_mayores_siete)
print("Cantidad de alumnos con notas menores a 7:", notas_menores_siete)
