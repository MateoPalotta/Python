x = int(input("Ingrese el valor de x: "))
y = int(input("Ingrese el valor de y: "))

if x > 0 and y > 0:
    print("El punto se ubica en el 1º cuadrante.")
elif x < 0 and y > 0:
    print("El punto se ubica en el 2º cuadrante.")
elif x < 0 and y < 0:
    print("El punto se ubica en el 3º cuadrante.")
elif x > 0 and y < 0:
    print("El punto se ubica en el 4º cuadrante.")
else:
    print("El punto no se ubica en ningún cuadrante.")