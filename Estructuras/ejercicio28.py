cantidad_negativos = 0
cantidad_positivos = 0
cantidad_multiplos_15 = 0
acumulado_pares = 0

for i in range(10):
    valor = int(input(f"Ingrese el valor {i+1}: "))

    if valor < 0:
        cantidad_negativos += 1
    elif valor > 0:
        cantidad_positivos += 1

    if valor % 15 == 0:
        cantidad_multiplos_15 += 1

    if valor % 2 == 0:
        acumulado_pares += valor

print("\nResultados:")
print(f"Cantidad de valores negativos: {cantidad_negativos}")
print(f"Cantidad de valores positivos: {cantidad_positivos}")
print(f"Cantidad de múltiplos de 15: {cantidad_multiplos_15}")
print(f"Valor acumulado de los números pares: {acumulado_pares}")
