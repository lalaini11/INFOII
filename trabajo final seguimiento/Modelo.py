import json
import os

class Sistema:
    def __init__(self, data_file='pacientes.json'):
        self.data_file = data_file
        self.cargarDatos()

    def cargarDatos(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                self.pacientes = json.load(file)
        else:
            self.pacientes = []

    def guardarInfo(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.pacientes, file, indent=4)

    def agregarPaciente(self, paciente:dict):
        if any(p['id'] == paciente['id'] for p in self.pacientes):
            return False  # ID ya existe
        self.pacientes.append(paciente)
        self.guardarInfo()
        return True

    def eliminarPacientes(self, pacienteID:str):
        self.pacientes = [p for p in self.pacientes if p['id'] != pacienteID]
        self.guardarInfo()

    def buscarPacientes(self, initNombre:str):
        initNombre = initNombre.lower().strip()
        resultados = [p for p in self.pacientes if p['nombre'].lower().strip().startswith(initNombre)]
        print(f"Resultados de la búsqueda para '{initNombre}': {resultados}")  # Mensaje de depuración
        return resultados


class Personal:
  def __init__(self):
    self.usuarioValido= {'admin123': 'contrasena123'}


  def verificar(self, usuario, password):
    return self.usuarioValido.get(usuario)==password