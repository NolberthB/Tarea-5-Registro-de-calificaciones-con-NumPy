# Tarea 5: Registro de Calificaciones con NumPy

## Objetivo

El objetivo de esta tarea es implementar un código en Python utilizando la librería NumPy para gestionar y analizar las calificaciones de un grupo de estudiantes. Se busca adquirir habilidades prácticas en la manipulación de arreglos y el cálculo de estadísticas básicas sobre datos numéricos.

## Explicación del Código

El código crea un array de NumPy que contiene las calificaciones de 5 estudiantes en 3 evaluaciones. A continuación, realiza los siguientes cálculos estadísticos:

1. **Promedio final del grupo**: Calcula el promedio de las calificaciones finales de cada estudiante.
2. **Calificación final más alta**: Obtiene la calificación más alta del grupo considerando los promedios finales de todos los estudiantes.
3. **Calificación final más baja**: Encuentra la calificación más baja del grupo.
4. **Calificación más alta del primer parcial**: Encuentra la calificación más alta obtenida en el primer parcial.
5. **Calificación más baja del segundo parcial**: Encuentra la calificación más baja obtenida en el segundo parcial.

El código hace uso de las funciones de NumPy como `np.mean()`, `np.max()`, y `np.min()` para obtener los resultados. Finalmente, imprime un resumen estadístico con los resultados de los cálculos.

```python
import numpy as np

# Crear el array con las calificaciones
calificaciones = np.array([
    [85, 90, 88],  # Estudiante 1
    [92, 78, 84],  # Estudiante 2
    [75, 80, 70],  # Estudiante 3
    [88, 85, 87],  # Estudiante 4
    [91, 95, 93]   # Estudiante 5
])

# Calcular las estadísticas solicitadas
promedio_final = np.mean(calificaciones, axis=1)
calificacion_final_max = np.max(promedio_final)
calificacion_final_min = np.min(promedio_final)
calificacion_max_parcial1 = np.max(calificaciones[:, 0])
calificacion_min_parcial2 = np.min(calificaciones[:, 1])

# Imprimir el resumen estadístico
print("Resumen Estadístico de Calificaciones:")
print(f"Promedio final del grupo: {promedio_final}")
print(f"Calificación final más alta del grupo: {calificacion_final_max}")
print(f"Calificación final más baja del grupo: {calificacion_final_min}")
print(f"Calificación más alta del primer parcial: {calificacion_max_parcial1}")
print(f"Calificación más baja del segundo parcial: {calificacion_min_parcial2}")
```

## Referencias
NumPy. (2023). Creating arrays. NumPy. https://numpy.org/doc/stable/user/basics.creation.html

NumPy. (2023). numpy.mean. NumPy. https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean

NumPy. (2023). numpy.min. NumPy. https://numpy.org/doc/stable/reference/generated/numpy.min.html

NumPy. (2023). numpy.max. NumPy. https://numpy.org/doc/stable/reference/generated/numpy.max.html
