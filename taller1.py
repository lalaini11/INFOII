class implantesMedicos:
    def __init__(self, marca, material, numRegistro):
        self.__marca=marca
        self.__material=material
        self.__numRegistro=numRegistro

    def mostrarInformacion(self):
        print(f"""El implante médico tiene la siguiente información:
        Marca: {self.__marca}
        Material: {self.__material}
        Registro: {self.__numRegistro}
""")
class protesisCadera(implantesMedicos):
    def __init__(self, marca, material, numRegistro,tipoFijacion,tamaño):
        super().__init__(marca, material, numRegistro)
        self.tipoFijacion=tipoFijacion
        self.tamaño=tamaño

class marcapasos(implantesMedicos):
    def __init__(self, marca, material, numRegistro,numElectrodos,alambrico,frecuencia):
        super().__init__(marca, material, numRegistro)
        self.numElectrodos=numElectrodos
        self.alambrico=alambrico
        self.frecuenciaEstimulacion=frecuencia

class stentsCoronarios(implantesMedicos):
    def __init__(self, marca, material, numRegistro,longitud,diametro):
        super().__init__(marca, material, numRegistro)
        self.longitud=longitud
        self.diametro=diametro

class implantesDentales(implantesMedicos):
    def __init__(self, marca, material, numRegistro,forma,sistemaFijacion):
        super().__init__(marca, material, numRegistro)
        self.forma=forma
        self.sistemaFijacion=sistemaFijacion

class protesisRodilla(implantesMedicos):
    def __init__(self, marca, material, numRegistro,fijacion,tamaño):
        super().__init__(marca, material, numRegistro)
        self.fijacion=fijacion
        self.tamaño=tamaño
class Paciente:
    def __init__(self,nombre,identificacion,fechaImplantacion,medicoAsociado,estadoImplante):
        self.__nombre=nombre
        self.__identificacion=identificacion
        self.__fechaImplantacion=fechaImplantacion
        self.__medicoAsociado=medicoAsociado
        self.__estadoImplante=estadoImplante
        self.pacientes=[]



    def agregarPaciente(self,pacientes):
        if pacientes in self.pacientes:
            print(f"El paciente {self.__nombre} ya se encuentra registrado")
        else:
            self.pacientes.append(pacientes)
            print(f"El paciente {self.__nombre} se registró exitosamente")
    
    def verInformacion(self):
        print(f"""El paciente tiene la siguiente información:
            Nombre: {self.__nombre}
            Identificación: {self.__identificacion}
            Fecha Implantación: {self.__fechaImplantacion}
            Médico asociado: {self.__medicoAsociado}
            Estado implante: {self.__estadoImplante}""")
            
class Seguimiento(Paciente):
    def __init__(self, nombre,identificacion,fechaImplantacion,medicoAsociado,estadoImplante,fechaRevision,mantenimiento):
        super().__init__(nombre,identificacion,fechaImplantacion,medicoAsociado,estadoImplante)
        self.fechaRevision=fechaRevision
        self.mantenimiento=mantenimiento
        self.seguimientos=[]
   
    def agregarInformacion(self,seguimientos):
        if seguimientos in self.seguimientos:
            print("El seguimiento ya se encuentra registrado")
        else:
            self.seguimientos.append(seguimientos)
            print(f"El seguimiento se registró exitosamente")

    def mostrarInformacion(self):
        print(f"""El seguimiento tiene la siguiente información:
            Fecha Revisión: {self.fechaRevision}
            Mantenimiento: {self.mantenimiento}""")

class interfazUsuario:
    def __init__(self):
        self.implantes = []

    def agregarImplante(self, implante):
        if implante in self.implantes:
            print(f"El implante {self.__numRegistro} ya se encuentra registrado")
        else:
            self.implantes.append(implante)
            print(f"El implante {self.__numRegistro} se registró exitosamente")

    def eliminarImplante(self, numRegistro):
        for implante in self.implantes:
            if implante._implantesMedicos__numRegistro == numRegistro:
                self.implantes.remove(implante)
                print(f"El implante {numRegistro} se eliminó correctamente")
                return
        print(f"El implante {numRegistro} no se encuentra registrado")    
        
    def verInventario(self, implante): #REVISAR
        for i in self.implantes:
            for i, implante in enumerate(self.implantes):
                print(f"Implante {i+1}: {implante}")