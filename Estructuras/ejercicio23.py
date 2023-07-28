suma_ultimos_5 = 0

for i in range(1, 11):
    numero = int(input(f"Ingrese el número {i}: "))

    if i > 5:
        suma_ultimos_5 += numero

print("La suma de los últimos 5 números ingresados es:", suma_ultimos_5)
