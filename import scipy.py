import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt

# Cargar el archivo .mat
path = r"C:\Users\griss\Downloads\senales_potencial.mat"
mat_contents = sio.loadmat(path) #asigna el contenido de ese archivo en el PATH #loadmath carga un archivo .mat

# Explorar el contenido
print(mat_contents.keys())

# Acceder a los datos de las señales
senal1 = mat_contents['frecuente']
senal2 = mat_contents['infrecuente']

# Obtener el tamaño, forma y dimensiones de cada señal
tamano_senal1 = senal1.shape
tamano_senal2 = senal2.shape

print("Tamaño de la señal 1:", tamano_senal1)
print("Tamaño de la señal 2:", tamano_senal2)

class analisisSenal:
    def __init__(self, archivo):
        self.datos = sio.loadmat(archivo)
        self.senal1 = self.datos['frecuente']
        self.senal2 = self.datos['infrecuente']
    
    def valor_maximo(self, sensor):
        if sensor == 1:
            max_valor = np.max(self.senal1)
            max_posicion = np.argmax(self.senal1)
        elif sensor == 2:
            max_valor = np.max(self.senal2)
            max_posicion = np.argmax(self.senal2)
        else:
            raise ValueError("El número de sensor debe ser 1 o 2.")
        
        return max_valor, max_posicion
    
    def graficar_senales(self, serie_temporal=0):
        max_valor_senal1, max_posicion_senal1 = self.valor_maximo(1)
        max_valor_senal2, max_posicion_senal2 = self.valor_maximo(2)
        
        plt.figure(figsize=(10, 6))
        plt.plot(self.senal1[serie_temporal], label='Señal 1', color='blue')
        plt.plot(self.senal2[serie_temporal], label='Señal 2', color='red')
        plt.scatter(max_posicion_senal1, max_valor_senal1, color='blue', label='Máximo Señal 1')
        plt.scatter(max_posicion_senal2, max_valor_senal2, color='red', label='Máximo Señal 2')
        plt.annotate(f'{max_valor_senal1:.2f}', xy=(max_posicion_senal1, max_valor_senal1),
                    xytext=(max_posicion_senal1 - 50, max_valor_senal1 + 50),
                    arrowprops=dict(facecolor='blue', shrink=0.05))
        plt.annotate(f'{max_valor_senal2:.2f}', xy=(max_posicion_senal2, max_valor_senal2),
                    xytext=(max_posicion_senal2 + 50, max_valor_senal2 + 50),
                    arrowprops=dict(facecolor='red', shrink=0.05))
        plt.title('Gráfico de las Señales')
        plt.xlabel('Tiempo')
        plt.ylabel('Amplitud')
        plt.legend()
        plt.show()

    
    def graficar_histogramas(self):
        senal1_aplanada = self.senal1.flatten()
        senal2_aplanada = self.senal2.flatten()
        
        plt.figure(figsize=(12, 6))
        plt.subplot(1, 2, 1)
        plt.hist(senal1_aplanada, bins=20, color='blue', alpha=0.7, label='Señal 1')
        plt.axvline(np.mean(senal1_aplanada), color='blue', linestyle='dashed', linewidth=1)
        plt.axvline(np.median(senal1_aplanada), color='blue', linestyle='dotted', linewidth=1)
        plt.title('Histograma Señal 1')
        plt.xlabel('Amplitud')
        plt.ylabel('Frecuencia')
        plt.legend()
        
        plt.subplot(1, 2, 2)
        plt.hist(senal2_aplanada, bins=20, color='red', alpha=0.7, label='Señal 2')
        plt.axvline(np.mean(senal2_aplanada), color='red', linestyle='dashed', linewidth=1)
        plt.axvline(np.median(senal2_aplanada), color='red', linestyle='dotted', linewidth=1)
        plt.title('Histograma Señal 2')
        plt.xlabel('Amplitud')
        plt.ylabel('Frecuencia')
        plt.legend()
        
        plt.tight_layout()
        plt.show()

# Uso de la clase analisisSenal

file_path = r"C:\Users\griss\Downloads\senales_potencial.mat"
analisis = analisisSenal(file_path)
analisis.graficar_senales(serie_temporal=0)
analisis.graficar_histogramas()
