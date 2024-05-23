import pydicom
import nibabel as nib
import os
import numpy as np
from pydicom.uid import generate_uid

class Estudio:
    def __init__(self, dicompath):
        self.path = dicompath
        self.data = pydicom.dcmread(dicompath)
        self.id = self.data.SOPInstanceUID

    def anonimizarDicom(self, inputPath, outputPath):
        ds = pydicom.dcmread(inputPath)
        etiquetas = ["PatientName", "PatientID"]
        for tag in etiquetas:
            if tag in ds:
                delattr(ds, tag)
        ds.SOPInstanceUID = generate_uid()
        ds.save_as(outputPath)
        print(f"Archivo anonimizado guardado en: {outputPath}")

    @staticmethod
    def anonimizarCarpeta(inputDir, outputDir):
        # Crear la carpeta de salida si no existe
        if not os.path.exists(outputDir):
            os.makedirs(outputDir)
        
        for filename in os.listdir(inputDir):
            if filename.endswith(".dcm"):
                inputPath = os.path.join(inputDir, filename)
                outputPath = os.path.join(outputDir, filename)
                estudio = Estudio(inputPath)
                estudio.anonimizarDicom(inputPath, outputPath)

    @staticmethod
    def convertirNifti(dicomdir, niftipath):
        dicomFiles = [os.path.join(dicomdir, f) for f in os.listdir(dicomdir) if f.endswith('.dcm')]
        imagenes = [pydicom.dcmread(dcm) for dcm in dicomFiles]
        imagenes.sort(key=lambda x: int(x.InstanceNumber))  # ordena las imagenes
        imarray = np.stack([dcm.pixel_array for dcm in imagenes])  # almacena las imagenes en un array
        imagenNifti = nib.Nifti1Image(imarray, np.eye(4))  # crea nifti
        nib.save(imagenNifti, niftipath)  # guarda nifti en el path
        print(f"Conversión completa: {niftipath}")

    def obtenerInfo(self):
        info = {
            "Fecha": self.data.StudyDate,
            "Modalidad": self.data.Modality,
            "Descripción": self.data.StudyDescription,
            "Dimensiones": self.data.pixel_array.shape
        }
        return info

# Uso de la clase para anonimizar una carpeta
input_dir = r"C:\Users\griss\Documents\Parcial 1 Info2\INFOII\0001\0001"
output_dir = r"C:\Users\griss\Documents\Parcial 1 Info2\INFOII\0001_anonimizados"
Estudio.anonimizarCarpeta(input_dir, output_dir)
