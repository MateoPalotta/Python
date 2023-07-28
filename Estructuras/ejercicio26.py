def determinar_tipo(lado1, lado2, lado3):
    if lado1 == lado2 == lado3:
        return "equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return "isósceles"
    else:
        return "escaleno"

cantidad_equilateros = 0
cantidad_isosceles = 0
cantidad_escalenos = 0

n = int(input("Ingrese la cantidad de triángulos: "))

for i in range(n):
    print(f"\nTriángulo {i+1}:")
    lado1 = float(input("Ingrese el lado 1: "))
    lado2 = float(input("Ingrese el lado 2: "))
    lado3 = float(input("Ingrese el lado 3: "))

    tipo = determinar_tipo(lado1, lado2, lado3)

    if tipo == "equilátero":
        cantidad_equilateros += 1
    elif tipo == "isósceles":
        cantidad_isosceles += 1
    else:
        cantidad_escalenos += 1

    print(f"Tipo de triángulo: {tipo}")

print("\nResultados:")
print(f"Cantidad de triángulos equiláteros: {cantidad_equilateros}")
print(f"Cantidad de triángulos isósceles: {cantidad_isosceles}")
print(f"Cantidad de triángulos escalenos: {cantidad_escalenos}")
