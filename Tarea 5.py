# Importar la libreria NumPy
import numpy as np

# Paso 1: Crear el array con las calificaciones de los estudiantes
# Suponemos que tenemos 5 estudiantes y 3 evaluaciones (parciales).
# Cada fila representa un estudiante y cada columna una evaluación.

calificaciones = np.array([
    [85, 90, 88],  # Estudiante 1
    [92, 78, 84],  # Estudiante 2
    [75, 80, 70],  # Estudiante 3
    [88, 85, 87],  # Estudiante 4
    [91, 95, 93]   # Estudiante 5
])

# Paso 2: Calcular las estadísticas solicitadas

# Promedio final del grupo (promedio de cada estudiante)
promedio_final = np.mean(calificaciones, axis=1)

# Calificación final más alta del grupo
calificacion_final_max = np.max(promedio_final)

# Calificación final más baja del grupo
calificacion_final_min = np.min(promedio_final)

# Calificación más alta del primer parcial (primera columna)
calificacion_max_parcial1 = np.max(calificaciones[:, 0])

# Calificación más baja del segundo parcial (segunda columna)
calificacion_min_parcial2 = np.min(calificaciones[:, 1])

# Paso 3: Imprimir el resumen estadístico
print("Resumen Estadístico de Calificaciones:")
print(f"Promedio final del grupo: {np.round(promedio_final, 1)}")
print(f"Calificación final más alta del grupo: {np.round(calificacion_final_max, 1)}")
print(f"Calificación final más baja del grupo: {np.round(calificacion_final_min, 1)}")
print(f"Calificación más alta del primer parcial: {np.round(calificacion_max_parcial1, 1)}")
print(f"Calificación más baja del segundo parcial: {np.round(calificacion_min_parcial2, 1)}")

