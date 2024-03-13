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
    
    def modificarProtesis(self, numRegistro, nuevaMarca=None, nuevoMaterial=None, nuevo_numRegistro=None, nuevo_tipoFijacion=None,nuevoTamaño=None):
        for implante in self.implantes:
            if implante._implantesMedicos__numRegistro == numRegistro:
                if nuevaMarca:
                    implante._implantesMedicos__marca = nuevaMarca
                if nuevoMaterial:
                    implante._implantesMedicos__material = nuevoMaterial
                if nuevo_numRegistro:
                    implante._implantesMedicos__numRegistro = nuevo_numRegistro
                print(f"El implante {numRegistro} se ha modificado correctamente")
                if nuevo_tipoFijacion:
                    implante._implantesMedicos__numRegistro = nuevo_tipoFijacion
                if nuevoTamaño:
                    implante._implantesMedicos__numRegistro = nuevoTamaño
                return
        print(f"El implante {numRegistro} no se encuentra registrado")


    def modificarMarcapasos(self, numRegistro, nuevaMarca=None, nuevoMaterial=None, nuevo_numRegistro=None,nuevo_numElectrodos=None,nuevoAlambrico=None,nuevoFrecuencia=None):
        for implante in self.implantes:
            if implante._implantesMedicos__numRegistro == numRegistro:
                if nuevaMarca:
                    implante._implantesMedicos__marca = nuevaMarca
                if nuevoMaterial:
                    implante._implantesMedicos__material = nuevoMaterial
                if nuevo_numRegistro:
                    implante._implantesMedicos__numRegistro = nuevo_numRegistro
                print(f"El implante {numRegistro} se ha modificado correctamente")
                if nuevo_numElectrodos:
                    implante._implantesMedicos__numRegistro = nuevo_numElectrodos
                if nuevoAlambrico:
                    implante._implantesMedicos__numRegistro = nuevoAlambrico
                if nuevoFrecuencia:
                    implante._implantesMedicos__numRegistro = nuevoFrecuencia
                return
        print(f"El implante {numRegistro} no se encuentra registrado")

    def modificar_stentsCoronarios(self, numRegistro, nuevaMarca=None, nuevoMaterial=None, nuevo_numRegistro=None,nuevolongitud=None,nuevoDiametro=None):
        for implante in self.implantes:
            if implante._implantesMedicos__numRegistro == numRegistro:
                if nuevaMarca:
                    implante._implantesMedicos__marca = nuevaMarca
                if nuevoMaterial:
                    implante._implantesMedicos__material = nuevoMaterial
                if nuevo_numRegistro:
                    implante._implantesMedicos__numRegistro = nuevo_numRegistro
                print(f"El implante {numRegistro} se ha modificado correctamente")
                if nuevolongitud:
                    implante._implantesMedicos__numRegistro = nuevolongitud
                if nuevoDiametro:
                    implante._implantesMedicos__numRegistro = nuevoDiametro
                return
        print(f"El implante {numRegistro} no se encuentra registrado")

    def modificar_implantesDentales(self, numRegistro, nuevaMarca=None, nuevoMaterial=None, nuevo_numRegistro=None,nuevoForma=None,nuevo_sistemaFijacion=None):
        for implante in self.implantes:
            if implante._implantesMedicos__numRegistro == numRegistro:
                if nuevaMarca:
                    implante._implantesMedicos__marca = nuevaMarca
                if nuevoMaterial:
                    implante._implantesMedicos__material = nuevoMaterial
                if nuevo_numRegistro:
                    implante._implantesMedicos__numRegistro = nuevo_numRegistro
                print(f"El implante {numRegistro} se ha modificado correctamente")
                if nuevoForma:
                    implante._implantesMedicos__numRegistro = nuevoForma
                if nuevo_sistemaFijacion:
                    implante._implantesMedicos__numRegistro = nuevo_sistemaFijacion
                return
        print(f"El implante {numRegistro} no se encuentra registrado")
    
    def verInventario(self, implante): #REVISAR
        for i in self.implantes:
            for i, implante in enumerate(self.implantes):
                print(f"Implante {i+1}: {implante}")



interfaz = interfazUsuario()

while True:
    menu=int(input("""Ingrese lo que desea hacer:
                   1. Agregar implante
                   2. Eliminar implante
                   3. Editar implante
                   4. Ver inventario
                   5. Salir"""))
    if menu==5:
        print("Saliendo...")
        break
    elif menu == 1:
        marca = input("Ingrese la marca del implante: ")
        material = input("Ingrese el material del implante: ")
        numRegistro = input("Ingrese el número de registro del implante: ")
        nuevo_implante = implantesMedicos(marca, material, numRegistro)
        interfaz.agregarImplante(nuevo_implante)
    elif menu == 2:
        numRegistro = input("Ingrese el número de registro del implante a eliminar: ")
        interfaz.eliminarImplante(numRegistro)
    elif menu == 3:
        subMenu3=int(input("""Ingrese el implante a modificar:
                           1. Protesis de cadera o rodilla
                           2. Implante dental
                           3. Stent coronario
                           4. Marcapasos
                           """))
        if subMenu3==1:
            
            numRegistro = input("Ingrese el número de registro del implante a modificar: ")
            nuevaMarca = input("Ingrese la nueva marca del implante (deje en blanco para no modificar): ")
            nuevoMaterial = input("Ingrese el nuevo material del implante (deje en blanco para no modificar): ")
            nuevo_numRegistro = input("Ingrese el nuevo número de registro del implante (deje en blanco para no modificar): ")
            nuevoTamaño= input("Ingrese el nuevo tamaño del implante (deje en blanco para no modificar): ")
            nuevo_tipoFijacion= input("Ingrese el nuevo tipo de fijación del implante (deje en blanco para no modificar): ")
            interfaz.modificarProtesis(numRegistro, nuevaMarca, nuevoMaterial, nuevo_numRegistro, nuevoTamaño,nuevo_tipoFijacion)
        
        if subMenu3==2:
            
            numRegistro = input("Ingrese el número de registro del implante a modificar: ")
            nuevaMarca = input("Ingrese la nueva marca del implante (deje en blanco para no modificar): ")
            nuevoMaterial = input("Ingrese el nuevo material del implante (deje en blanco para no modificar): ")
            nuevo_numRegistro = input("Ingrese el nuevo número de registro del implante (deje en blanco para no modificar): ")
            nuevoForma= input("Ingrese la nueva forma del implante (deje en blanco para no modificar): ")
            nuevo_sistemaFijacion= input("Ingrese el nuevo sistema de fijación del implante (deje en blanco para no modificar): ")
            interfaz.modificar_implantesDentales(numRegistro, nuevaMarca, nuevoMaterial, nuevo_numRegistro, nuevoForma,nuevo_sistemaFijacion)
        
        
        if subMenu3==3:
            
            numRegistro = input("Ingrese el número de registro del implante a modificar: ")
            nuevaMarca = input("Ingrese la nueva marca del implante (deje en blanco para no modificar): ")
            nuevoMaterial = input("Ingrese el nuevo material del implante (deje en blanco para no modificar): ")
            nuevoLongitud = input("Ingrese la nueva longitud de registro del implante (deje en blanco para no modificar): ")
            nuevoDiametro= input("Ingrese el nuevo diametro del implante (deje en blanco para no modificar): ")
            interfaz.modificar_stentsCoronarios(numRegistro, nuevaMarca, nuevoMaterial, nuevo_numRegistro, nuevoLongitud,nuevoDiametro)

        if subMenu3==4:
            
            numRegistro = input("Ingrese el número de registro del implante a modificar: ")
            nuevaMarca = input("Ingrese la nueva marca del implante (deje en blanco para no modificar): ")
            nuevoMaterial = input("Ingrese el nuevo material del implante (deje en blanco para no modificar): ")
            nuevo_numElectrodos = input("Ingrese la nueva longitud de registro del implante (deje en blanco para no modificar): ")
            nuevoAlambrico= input("Ingrese el nuevo diametro del implante (deje en blanco para no modificar): ")
            nuevoFrecuencia= input("Ingrese el nuevo diametro del implante (deje en blanco para no modificar): ")

            interfaz.modificarMarcapasos(numRegistro, nuevaMarca, nuevoMaterial, nuevo_numRegistro, nuevo_numElectrodos,nuevoAlambrico,nuevoFrecuencia)



    elif menu == 4:
        interfaz.verInventario()
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
