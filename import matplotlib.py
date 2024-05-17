import matplotlib.pyplot as plt
tiempos = [15, 30, 45, 60]
produccion_CO2 = {
    'A': [1, 2, 2, 2],
    'B': [0, 0, 2, 10],
    'C': [4, 6, 10, 14],
    'D': [0, 0, 0, 0],
    'E': [0, 1, 1, 1.1],
    'F': [1, 2, 3, 3],
    'G': [1, 2, 2, 2]
}

# Crear el gráfico
plt.figure(figsize=(10, 6))

for tubo, produccion in produccion_CO2.items():
    plt.plot(tiempos, produccion, marker='o', label=tubo)

# Personalizar el gráfico
plt.title('Producción de CO2 en función del tiempo')
plt.xlabel('Tiempo (minutos)')
plt.ylabel('Producción de CO2 (mL)')
plt.legend()
plt.grid(True)

# Mostrar el gráfico
plt.tight_layout()
plt.show()
