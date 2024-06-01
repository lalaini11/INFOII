#### controlador
from Modelo import *

class controladorPersonal:
    def __init__(self, personal:object = Personal()):
        self.personal = personal

    def log_in(self, usuario, password):
        result = self.personal.verificar(usuario, password)
        return result

class controladorSistema:
    def __init__(self, sistema = Sistema()):
        self.sistema = sistema or Sistema()

    def agregar(self, data:dict):
        return self.sistema.agregarPaciente(data)

    def buscar_pacientes(self, initName:str = ''):
        return self.sistema.buscarPacientes(initName)

    def eliminar(self, id:str):
        return self.sistema.eliminarPacientes(id)