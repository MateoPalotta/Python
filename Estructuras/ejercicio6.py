numero = int(input("Ingrese un número entero positivo de hasta tres cifras: "))

if numero >= 0 and numero <= 9:
    print("El número tiene 1 cifra ")
elif numero >= 10 and numero <= 99:
    print("El número tiene 2 cifras ")
elif numero >= 100 and numero <= 999:
    print("El número tiene 3 cifras ")