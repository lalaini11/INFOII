# main.py
import sys
from PyQt5.QtWidgets import QApplication
from Controlador import controladorSistema, controladorPersonal
from Modelo import Sistema, Personal  # Ensure to import the Personal class
from Vista import ventanaLogin

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create an instance of the Personal class (which acts as the model)
    personal_model = Personal()

    # Create an instance of the controladorPersonal class, passing the Personal instance
    controlador = controladorPersonal(personal_model)

    # Create an instance of the ventanaLogin class
    login_window = ventanaLogin()

    # Assign the controller to the login window
    login_window.asignarControlador(controlador)

    # Show the login window
    login_window.show()

    # Execute the application
    sys.exit(app.exec_())
