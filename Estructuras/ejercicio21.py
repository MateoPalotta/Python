n = int(input("Ingrese la cantidad de números a ingresar: "))

pares = 0
impares = 0
contador = 0

while contador < n:
    numero = int(input("Ingrese un número entero: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    contador += 1

print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
