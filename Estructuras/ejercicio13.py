sueldo = float(input("Ingrese el sueldo del operario: "))
antiguedad = int(input("Ingrese los años de antigüedad del operario: "))

if sueldo < 500 and antiguedad >= 10:
    sueldo_a_pagar = sueldo * 1.2
    print("Sueldo a pagar con aumento del 20%:", sueldo_a_pagar)
elif sueldo < 500 and antiguedad < 10:
    sueldo_a_pagar = sueldo * 1.05
    print("Sueldo a pagar con aumento del 5%:", sueldo_a_pagar)
else:
    print("Sueldo a pagar sin cambios:", sueldo)
