
saludables = 0
total_estudiantes = int(input("¿Cuántos estudiantes vas a evaluar? "))

for i in range(total_estudiantes):
    print("\nEstudiante", i + 1)

    # Pedir datos
    sueño = int(input("Horas de sueño al día: "))
    ejercicio = int(input("Veces que hace ejercicio por semana: "))
    frutas = int(input("Porciones de frutas/verduras al día: "))

   
    if sueño >= 7 and ejercicio >= 3 and frutas >= 5:
        saludables += 1

no_saludables = total_estudiantes - saludables
porcentaje = (saludables / total_estudiantes) * 100


print("\n--- RESULTADOS ---")
print(f"Estudiantes saludables: {saludables}")
print(f"Estudiantes no saludables: {no_saludables}")
print(f"Porcentaje saludables:, {porcentaje}, %")


if porcentaje > 70:
    print("Buen estado general de salud en la comunidad.")
elif porcentaje >= 40:
    print("Nivel aceptable, pero se debe mejorar.")
else:
    print("Alerta roja: se requieren campañas urgentes.")