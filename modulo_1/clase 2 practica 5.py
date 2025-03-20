#Actividad salon 
#practica 5 clase 2
# Preguntar cuántos estudiantes hay en la clase
num_estudiantes = int(input("¿Cuántos estudiantes hay en la clase? "))

# Usar un bucle para solicitar y almacenar las calificaciones en una lista
calificaciones = []
for i in range(num_estudiantes):
    calificacion = float(input(f"Ingrese la calificación del estudiante {i + 1}: "))
    calificaciones.append(calificacion)

#Calcular la suma y el promedio de las calificaciones
suma_calificaciones = sum(calificaciones)
promedio = suma_calificaciones / num_estudiantes

#Encontrar la calificación más alta y la más baja
calificacion_maxima = max(calificaciones)
calificacion_minima = min(calificaciones)

#Mostrar los resultados
print("Resultados:")
print(f"Promedio de calificaciones: {promedio}")
print(f"Calificación más alta: {calificacion_maxima}")
print(f"Calificación más baja: {calificacion_minima}")