import random

def jugar_adivina_numero():
    numero_secreto = random.randint(1, 100)
    intentos_realizados = 0
    max_intentos = 10

    print("Juego - Adivina el número")
    
    print("El juego consiste en que se genera un numero del 1 al 100 y hay que adivinarlo")
    
    print("Generando un numero del 1 al 100. Adivinalo")

    while intentos_realizados < max_intentos:
        intento = int(input("Tu número: "))

        intentos_realizados += 1

        if intento < numero_secreto:
            print("No. Es muy bajo, Intenta de nuevo")
        elif intento > numero_secreto:
            print("No. Es muy alto, Intenta de nuevo")
        else:
            print(f"Bien adivinaste el número en {intentos_realizados} intentos.")
            break

    if intentos_realizados == max_intentos:
        print(f"Agotaste tus {max_intentos} intentos. El número secreto era {numero_secreto}.")

jugar_adivina_numero()
