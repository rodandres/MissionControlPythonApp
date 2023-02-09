import matplotlib.pyplot as plt

# Crear una figura y un eje
fig, ax = plt.subplots()

# Dibujar algunos datos en el eje
ax.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 4, 9, 16, 25, 36, 49, 64, 81, 100])

# Crear una lista de posiciones del eje x cada 0.2 unidades
x_positions = [i*0.2 for i in range(11)]

# Crear una lista de etiquetas para las posiciones del eje x
x_labels = [str(i*0.2) for i in range(11)]

# Establecer las etiquetas del eje x
ax.set_xticks(x_positions)
ax.set_xticklabels(x_labels)

# Mostrar la figura
plt.show()
