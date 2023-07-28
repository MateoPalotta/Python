n = int(input("Ingrese la cantidad de empleados: "))

sueldos = []
sueldos_100_300 = 0
sueldos_mas_300 = 0

i = 0
while i < n:
    sueldo = float(input("Ingrese el sueldo del empleado: "))
    sueldos.append(sueldo)
    if 100 <= sueldo <= 300:
        sueldos_100_300 += 1
    elif sueldo > 300:
        sueldos_mas_300 += 1
    i += 1

gasto_total = sum(sueldos)

print("Cantidad de empleados que cobran entre $100 y $300:", sueldos_100_300)
print("Cantidad de empleados que cobran más de $300:", sueldos_mas_300)
print("Importe total que la empresa gasta en sueldos al personal: $", gasto_total)
