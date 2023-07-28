valor = int(input("Ingrese un valor del 1 al 10: "))

if valor >= 1 and valor <= 10:
    for i in range(1, 13):
        resultado = valor * i
        print(resultado)
else:
    print("El valor ingresado no es válido. Debe ser un número del 1 al 10 ")
