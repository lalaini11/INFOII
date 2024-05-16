import os
import pydicom
import matplotlib.pyplot as plt


def cargar(carpeta):
    imagenes = []
    for filename in sorted(os.listdir(carpeta)):
        #itera sobre los nombres de archivo en una carpeta específica, en orden alfabético, uno por uno, asignando cada nombre de archivo a la variable filename en cada iteración del bucle
        if filename.endswith('.dcm'):
            path = os.path.join(carpeta, filename)
            imagen = pydicom.dcmread(path)
            imagenes.append(imagen)
    return imagenes

#path a carpeta que contiene las imágenes DICOM
carpeta = "C:/Users/griss/Downloads/archivosDCM"
images = cargar(carpeta)

def viewImages(imagenes):
    for i, imagen in enumerate(imagenes, start=1):

        plt.imshow(imagen.pixel_array, cmap=plt.cm.gray)
        plt.title(f"Imagen {i}")
        plt.axis('off')
        plt.show()
        input("Presiona Enter para ver la siguiente imagen...")
        

# Visualizar las imágenes DICOM en un bucle
viewImages(images)
print("Saliendo..")
