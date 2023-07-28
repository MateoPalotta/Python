edades_manana = []
for i in range(5):
    edad = int(input("Ingrese la edad del estudiante del turno mañana: "))
    edades_manana.append(edad)

edades_tarde = []
for i in range(6):
    edad = int(input("Ingrese la edad del estudiante del turno tarde: "))
    edades_tarde.append(edad)

edades_noche = []
for i in range(11):
    edad = int(input("Ingrese la edad del estudiante del turno noche: "))
    edades_noche.append(edad)

promedio_manana = sum(edades_manana) / len(edades_manana)
promedio_tarde = sum(edades_tarde) / len(edades_tarde)
promedio_noche = sum(edades_noche) / len(edades_noche)

print("Promedio de edades del turno mañana: ", promedio_manana)
print("Promedio de edades del turno tarde: ", promedio_tarde)
print("Promedio de edades del turno noche: ", promedio_noche)

if promedio_manana > promedio_tarde and promedio_manana > promedio_noche:
    print("El turno mañana tiene un promedio de edades mayor ")
elif promedio_tarde > promedio_manana and promedio_tarde > promedio_noche:
    print("El turno tarde tiene un promedio de edades mayor ")
elif promedio_noche > promedio_manana and promedio_noche > promedio_tarde:
    print("El turno noche tiene un promedio de edades mayor ")
else:
    print("Hay dos o más turnos con el mismo promedio de edades mayor ")
