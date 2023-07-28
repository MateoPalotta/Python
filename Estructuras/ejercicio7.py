total_preguntas = int(input("Ingrese la cantidad total de preguntas: "))
preguntas_correctas = int(input("Ingrese la cantidad de preguntas contestadas correctamente: "))

porcentaje_correctas = (preguntas_correctas / total_preguntas) * 100

if porcentaje_correctas >= 90:
    nivel = "Nivel máximo"
elif porcentaje_correctas >= 75:
    nivel = "Nivel medio"
elif porcentaje_correctas >= 50:
    nivel = "Nivel regular"
else:
    nivel = "Fuera de nivel"

print("Porcentaje de respuestas correctas: ", porcentaje_correctas)
print("Nivel del postulante: ", nivel)
