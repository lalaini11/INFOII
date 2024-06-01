from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QPushButton, QTableWidgetItem
from PyQt5.uic import loadUi
from PyQt5 import QtGui
from Controlador import controladorPersonal, controladorSistema
import sys

class ventanaLogin(QDialog):
  def __init__(self): #Constructor de la clase
    super().__init__()
    loadUi('login.ui',self)
    self.setup()
    self.controladorPersonal =controladorPersonal()

  def setup(self): # Llama al método setup, que está definido más adelante en la clase.
    #se programa la senal para el boton
    self.boton_ingresar.clicked.connect(self.accion_ingresar) #cuando el botón se presiona, se ejecutará el método accion_ingresar.


  def accion_ingresar(self):
    #Extraer el texto de los campos campo_usuario y campo_password.
    usuario = self.campo_usuario.text()
    password = self.campo_contra.text()
    #esta informacion la debemos pasar al controlador
    resultado = self.controladorPersonal.log_in(usuario,password) #Función de validación del controlador
    #Se crea la ventana de resultado
    msg = QMessageBox(self)
    msg.setWindowTitle("Resultado")
    #se selecciona el resultado de acuerdo al resultado de la operacion
    if resultado == True:      
      self.ventanaSistema = ventanaSistema()
      self.ventanaSistema.show()
      self.close()
    else:
      msg.setText("Usuario no Valido")
      msg.exec()
        #se muestra la ventana
    msg.show()


class ventanaSistema(QDialog):

  def __init__(self):
    super().__init__()
    loadUi('sist.ui',self)

    self.controladorSistema = controladorSistema()
    self.setup()

  def setup(self):
    validator = QtGui.QIntValidator(1, 9999999, self)
    self.tableView.verticalHeader().setVisible(False)
    self.agregar.clicked.connect(self.agregar_pacientes)
    self.busqueda.clicked.connect(self.filtrarPacientes)
    self.id.setValidator(validator)
    self.edad.setValidator(validator)
    self.tablaActualizada()
    self.readPacientes()


  def readPacientes(self):
    if self.controladorSistema:
      return self.controladorSistema.buscar_pacientes()
    else:
      return []

  def filtrarPacientes(self):
    
    buscar = self.campoBuscar.text()  # Asegúrate de que 'campoBuscar' sea el nombre correcto
    print(f"Buscando: {buscar}")  # Mensaje de depuración
    if self.controladorSistema:
        self.listaPacientes = self.controladorSistema.buscar_pacientes(buscar)
        print(f"Pacientes encontrados: {self.listaPacientes}")  # Mensaje de depuración
        self.tablaActualizada()
    else:
        print("Controlador no asignado")

  def agregar_pacientes(self):

    id = self.id.text()
    nombre = self.nombre.text()
    apellido = self.apellido.text()
    edad = self.edad.text()
    if not id or not nombre or not apellido or not edad:
      msgBox = QMessageBox()
      msgBox.setIcon(QMessageBox.Warning)
      msgBox.setText("Debe ingresar todos los datos")
      msgBox.setWindowTitle('Datos faltantes')
      msgBox.setStandardButtons(QMessageBox.Ok)
      msgBox.exec()
    else:
      paciente = {'id':id, 'nombre':nombre, 'apellido': apellido, 'edad': edad}
      isUnique = self.controladorSistema.agregar(paciente)
      if not isUnique:
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText("La id ya existe")
        msgBox.setWindowTitle('Id repetida')
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()
      else:
        self.readPacientes()
        self.tablaActualizada()
        self.id.setText('')
        self.nombre.setText('')
        self.apellido.setText('')
        self.edad.setText('')


  def tablaActualizada(self):
    pacientes = self.listaPacientes if hasattr(self, 'listaPacientes') else self.readPacientes()
    print(f"Actualizando tabla con: {pacientes}")  # Mensaje de depuración
    self.tableView.setRowCount(len(pacientes))
    self.tableView.setColumnCount(5)
    columnas = ["id", "nombre", "apellido", "edad", '']
    columnLayout = ['id', 'nombre', 'apellido', 'edad', '']
    self.tableView.setHorizontalHeaderLabels(columnas)
    for row, Paciente in enumerate(pacientes):
        for column in range(4):
            item = QTableWidgetItem(Paciente[columnLayout[column]])
            self.tableView.setItem(row, column, item)

        btn = QPushButton('Eliminar', self)
        btn.clicked.connect(lambda ch, r=row: self.Eliminar(r))
        self.tableView.setCellWidget(row, 4, btn)

    self.tableView.setColumnWidth(0, 80)
    self.tableView.setColumnWidth(1, 110)
    self.tableView.setColumnWidth(2, 60)
    self.tableView.setColumnWidth(3, 60)
    self.tableView.setColumnWidth(4, 60)


  def Eliminar(self, row):
    id = self.tableView.item(row, 0).text()
    deleted = self.controladorSistema.eliminar(id)
    if deleted:
      msgBox = QMessageBox()
      msgBox.setIcon(QMessageBox.Warning)
      msgBox.setText("Error")
      msgBox.setWindowTitle('¡¡Error!!')
      msgBox.setStandardButtons(QMessageBox.Ok)
      msgBox.exec()
    self.readPacientes()
    self.tablaActualizada()



#se crean los objetos para la ejecucion
if __name__ == '__main__':
    app = QApplication(sys.argv)
    p = ventanaLogin()
    p.show()
    sys.exit(app.exec_())