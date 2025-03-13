#Actividad salon 
#practica 5 clase 2
num_estudiantes = int(input("¿Cuántos estudiantes hay en total? ")) #me dice un  numero de estudiantes que luego usare como repeticion\iteracion
calificaciones = [] # Bucle para las notas
for i in range(num_estudiantes): #rango pa que use el numero de estudiantes como repeticion
    calificacion = float(input(f"Ingrese la calificación del estudiante {i + 1}: ")) #+1 para que no inicie en 0
    calificaciones.append(calificacion)# para agregar las notas
suma_calificaciones = sum(calificaciones) #Calcular la suma, para poder sacar el promedio de las calificaciones
promedio = suma_calificaciones / num_estudiantes #promedio
calificacion_maxima = max(calificaciones) #calificación más alta 
calificacion_minima = min(calificaciones)  #calificación más baja
print("Resultados:") #Mostrar los resultados
print(f"Promedio de calificaciones: {promedio}")
print(f"Calificación más alta: {calificacion_maxima}")
print(f"Calificación más baja: {calificacion_minima}")
