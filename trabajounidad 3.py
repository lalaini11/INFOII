import pydicom
import nibabel as nib
from pydicom import anonymize
import os
import numpy as np

class Estudio:
    def __init__(self, dicompath):
        self.path = dicompath
        self.data = pydicom.dcmread(dicompath)
        self.id = self.dicomdata.SOPInstanceUID

    def anonimizar(self):
        self.dicomdata = anonymize(self.dicomdata)
    
    def convertirNifti(dicomdir, niftipath):
        dicomFiles = [os.path.join(dicomdir, f) for f in os.listdir(dicomdir) if f.endswith('.dcm')]
        imagenes = [pydicom.dcmread(dcm) for dcm in dicomFiles]
        imagenes.sort(key=lambda x: int(x.InstanceNumber))  #ordena las imagenes 
        imarray = np.stack([dcm.pixel_array for dcm in imagenes]) #almacena las imagenes en un array
        imagenNifti = nib.Nifti1Image(imarray, np.eye(4))  #crea nifti
        nib.save(imagenNifti, niftipath) #guarda nifiti en el path
        print(f"Conversión completa: {niftipath}")
    
    def obtenerInfo(self):
        info = {
            "Fecha": self.dicom_data.StudyDate,
            "Modalidad": self.dicom_data.Modality,
            "Descripción": self.dicom_data.StudyDescription,
            "Dimensiones": self.dicom_data.pixel_array.shape
        }
        return info


class Paciente:
    def __init__(self, idPaciente, nombre):
        self.id_paciente =idPaciente
        self.nombre =nombre
        self.estudios =[]

    def agregarEstudio(self, estudio):
        self.estudios.append(estudio)
    
    def eliminarEstudio(self, estudioID):
        self.estudios =[estudio for estudio in self.estudios if estudio.id != estudioID]

    def obtenerEstudios(self):
        return [estudio.obtenerInfo() for estudio in self.estudios]

class SistemaGestion:
    def __init__(self):
        self.pacientes = {}

    def agregarEstudio(self, idPaciente, nombrePaciente, estudio):
        if idPaciente not in self.pacientes:
            self.pacientes[idPaciente] = Paciente(idPaciente, nombrePaciente)
        self.pacientes[idPaciente].agregar_estudio(estudio)
    
    def consultarPaciente(self, idPaciente):
        if idPaciente in self.pacientes:
            return self.pacientes[idPaciente].obtenerEstudios()
        return None
    
    def eliminarEstudio(self, idPaciente, estudioID):
        if idPaciente in self.pacientes:
            self.pacientes[idPaciente].eliminarEstudio(estudioID)
    
    def visualizarEstudio(self, idPaciente, estudioID, modo='single'):
        
        pass

