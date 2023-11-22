import sys


from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QApplication, QFormLayout, QLineEdit, \
   QPushButton, QDialog, QDialogButtonBox, QVBoxLayout
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from clientes import Cliente




class Ventana1(QMainWindow):


   def __init__(self, parent=None):
       super(Ventana1, self).__init__(parent)


       self.setWindowTitle("Formulario de registro")


       # Poner el icono
       self.setWindowIcon(QtGui.QIcon('imagenes/gato.png.png'))


       self.ancho = 900
       self.alto = 600
       self.resize(self.ancho, self.alto)


       self.pantalla = self.frameGeometry()
       self.centro = QDesktopWidget().availableGeometry().center()
       self.pantalla.moveCenter(self.centro)
       self.move(self.pantalla.topLeft())


       self.setFixedWidth(self.ancho)
       self.setFixedHeight(self.alto)


       self.fondo = QLabel(self)
       self.imagenfondo = QPixmap('imagenes/fondo.jpg')
       self.fondo.setPixmap(self.imagenfondo)
       self.fondo.setScaledContents(True)


       # hacemos que se adapte el tamaño de la imagen
       self.resize(self.imagenfondo.width(), self.imagenfondo.height())


       self.setCentralWidget(self.fondo)


       # distribucion layaout horizontal
       self.horizontal = QHBoxLayout()
       # margenes
       self.horizontal.setContentsMargins(30, 30, 30, 30)


       # --------LAYOUT IZQUIERDO-----------


       self.ladoIzquierdo = QFormLayout()


       self.letrero1 = QLabel()
       self.letrero1.setText("Información del cliente")
       self.letrero1.setFont(QFont("Candara", 20))
       self.letrero1.setStyleSheet("color: #000080;")


       self.ladoIzquierdo.addRow(self.letrero1)


       self.letrero2 = QLabel()
       self.letrero2.setFixedWidth(340)
       self.letrero2.setText("Por favor ingrese la información del cliente"
                             "\nen el formulario de abajo. Los campos marcados"
                             "\ncon asterisco son obligatorios.")


       self.letrero2.setFont(QFont("Century", 10))
       self.letrero2.setStyleSheet("color: #000080; margin-bottom: 40px;"
                                   "martgin top: 20px;"
                                   "border: 2px solid #000080;"
                                   "border-left: none;"
                                   "border-right: none;"
                                   "border-top: none;")


       self.ladoIzquierdo.addRow(self.letrero2)


       self.nombreCompleto = QLineEdit()
       self.nombreCompleto.setFixedWidth(250)


       self.ladoIzquierdo.addRow("Nombre Completo*", self.nombreCompleto)


       self.usuario = QLineEdit()
       self.usuario.setFixedWidth(250)


       self.ladoIzquierdo.addRow("Ususario*", self.usuario)


       self.password = QLineEdit()
       self.password.setFixedWidth(250)
       self.password.setEchoMode(QLineEdit.Password)


       self.ladoIzquierdo.addRow("Password*", self.password)


       self.password2 = QLineEdit()
       self.password2.setFixedWidth(250)
       self.password2.setEchoMode(QLineEdit.Password)


       self.ladoIzquierdo.addRow("Password*", self.password2)


       self.documento = QLineEdit()
       self.documento.setFixedWidth(250)


       self.ladoIzquierdo.addRow("Documento*", self.documento)


       self.correo = QLineEdit()
       self.correo.setFixedWidth(250)


       self.ladoIzquierdo.addRow("Correo*", self.correo)


       self.botonRegistrar = QPushButton("Registrar")
       self.botonRegistrar.setFixedWidth(90)
       self.botonRegistrar.setStyleSheet("background-color: #008B45;"
                                         "color: #FFFFFF;"
                                         "padding: 10px;"
                                         "margin-top: 40px;")


       self.botonRegistrar.clicked.connect(self.accion_botonRegistrar)


       self.botonLimpiar = QPushButton("Limpiar")
       self.botonLimpiar.setFixedWidth(90)
       self.botonLimpiar.setStyleSheet("background-color: #008B45;"
                                       "color: #FFFFFF;"
                                       "padding: 10px;"
                                       "margin-top: 40px;")


       self.botonLimpiar.clicked.connect(self.accion_botonLimpiar)


       self.ladoIzquierdo.addRow(self.botonRegistrar, self.botonLimpiar)


       self.horizontal.addLayout(self.ladoIzquierdo)


       # ---------LAYOUT DERECHO-------


       self.ladoDerecho = QFormLayout()


       self.ladoDerecho.setContentsMargins(100, 0, 0, 0)


       self.letrero3 = QLabel()
       self.letrero3.setText("Recuperar contraseña")
       self.letrero3.setFont(QFont("Candara", 20))
       self.letrero3.setStyleSheet("color: #000080;")


       self.ladoDerecho.addRow(self.letrero3)


       self.letrero4 = QLabel()
       self.letrero4.setFixedWidth(400)
       self.letrero4.setText("Por favor ingrese la informarción para recuperar"
                             "\nla contraseña. Los campos marcados"
                             "\ncon asteriscos son obligatorios.")


       self.letrero4.setFont(QFont("Century", 10))


       self.letrero4.setStyleSheet("color: #000080; margin-bottom: 40px;"
                                   "martgin top: 20px;"
                                   "border: 2px solid #000080;"
                                   "border-left: none;"
                                   "border-right: none;"
                                   "border-top: none;")


       self.ladoDerecho.addRow(self.letrero4)


       # ------1
       self.labelPregunta1 = QLabel("Pregunta de verificación 1*")


       self.ladoDerecho.addRow(self.labelPregunta1)


       self.pregunta1 = QLineEdit()
       self.pregunta1.setFixedWidth(320)


       self.ladoDerecho.addRow(self.pregunta1)


       self.labelRespuesta1 = QLabel("Respuesta de verificación 1*")


       self.ladoDerecho.addRow(self.labelRespuesta1)


       self.respuesta1 = QLineEdit()
       self.respuesta1.setFixedWidth(320)


       self.ladoDerecho.addRow(self.respuesta1)


       # ------2
       self.labelPregunta2 = QLabel("Pregunta de verificación 2*")


       self.ladoDerecho.addRow(self.labelPregunta2)


       self.pregunta2 = QLineEdit()
       self.pregunta2.setFixedWidth(320)


       self.ladoDerecho.addRow(self.pregunta2)


       self.labelRespuesta2 = QLabel("Respuesta de verificación 2*")


       self.ladoDerecho.addRow(self.labelRespuesta2)


       self.respuesta2 = QLineEdit()
       self.respuesta2.setFixedWidth(320)


       self.ladoDerecho.addRow(self.respuesta2)


       # ------3
       self.labelPregunta3 = QLabel("Pregunta de verificación 3*")


       self.ladoDerecho.addRow(self.labelPregunta3)


       self.pregunta3 = QLineEdit()
       self.pregunta3.setFixedWidth(320)


       self.ladoDerecho.addRow(self.pregunta3)


       self.labelRespuesta3 = QLabel("Respuesta de verificación 3*")


       self.ladoDerecho.addRow(self.labelRespuesta3)


       self.respuesta3 = QLineEdit()
       self.respuesta3.setFixedWidth(320)


       self.ladoDerecho.addRow(self.respuesta3)


       self.botonBuscar = QPushButton("Buscar")
       self.botonBuscar.setFixedWidth(90)
       self.botonBuscar.setStyleSheet("background-color: #008B45;"
                                      "color: #FFFFFF;"
                                      "padding: 10px;"
                                      "margin-top: 40px;")


       self.botonBuscar.clicked.connect(self.accion_botonBuscar)






       self.botonRecuperar = QPushButton("Recuperar")
       self.botonRecuperar.setFixedWidth(90)
       self.botonRecuperar.setStyleSheet("background-color: #008B45;"
                                         "color: #FFFFFF;"
                                         "padding: 10px;"
                                         "margin-top: 40px;")


       self.botonRecuperar.clicked.connect(self.accion_botonRecuperar)


       self.ladoDerecho.addRow(self.botonBuscar, self.botonRecuperar)


       self.horizontal.addLayout(self.ladoDerecho)


       self.horizontal.addLayout(self.ladoDerecho)


       # ---------- FINAL---------
       # el layout principal del fondo es horizontal
       self.fondo.setLayout(self.horizontal)


       self.ventanaDialogo = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)


       self.ventanaDialogo.resize(300, 150)


       self.botonAceptar = QDialogButtonBox.Ok
       self.opciones = QDialogButtonBox(self.botonAceptar)
       self.opciones.accepted.connect(self.ventanaDialogo.accept)


       self.ventanaDialogo.setWindowTitle("Formulario de Registro")


       self.ventanaDialogo.setWindowModality(Qt.ApplicationModal)


       self.vertical = QVBoxLayout()


       self.mensaje = QLabel("")


       self.mensaje.setStyleSheet("background-color: #008B45; color: #FFFFFF; padding: 10px;")


       self.vertical.addWidget(self.mensaje)


       self.vertical.addWidget(self.opciones)


       self.ventanaDialogo.setLayout(self.vertical)




   def accion_botonLimpiar(self):
       self.nombreCompleto.setText('')
       self.usuario.setText('')
       self.password.setText('')
       self.password2.setText('')
       self.documento.setText('')
       self.correo.setText('')
       self.pregunta1.setText('')
       self.respuesta1.setText('')
       self.pregunta2.setText('')
       self.respuesta2.setText('')
       self.pregunta3.setText('')
       self.respuesta3.setText('')


   def accion_botonRegistrar(self):


       self.datosCorrectos = True




       if (
               self.password.text() != self.password2.text()
       ):
           self.datosCorrectos = False


           self.mensaje.setText("Los passwords no son iguales")


           self.ventanaDialogo.exec_()


       if (
               self.nombreCompleto.text() == ""
               or self.usuario.text() == ""
               or self.password.text() == ""
               or self.documento.text() == ""
               or self.correo.text() == ""
               or self.pregunta1.text() == ""
               or self.respuesta1.text() == ""
               or self.pregunta2.text() == ""
               or self.respuesta2.text() == ""
               or self.pregunta3.text() == ""
               or self.respuesta3.text() == ""
       ):
           self.datosCorrectos = False


           self.mensaje.setText("Debe ingresar todos los campos")


           self.ventanaDialogo.exec_()


       if self.datosCorrectos:


           self.file = open('datos/clientes.txt', 'ab')


           self.file.write(bytes(
               self.nombreCompleto.text() + ";"
               + self.usuario.text() + ";"
               + self.password.text() + ";"
               + self.password2.text() + ";"
               + self.documento.text() + ";"
               + self.correo.text() + ";"
               + self.pregunta1.text() + ";"
               + self.respuesta1.text() + ";"
               + self.pregunta2.text() + ";"
               + self.respuesta2.text() + ";"
               + self.pregunta3.text() + ";"
               + self.respuesta3.text() + "\n"
               , encoding='UTF-8'))


           self.file.close()


           self.file = open('datos/clientes.txt', 'rb')


           while self.file:
               linea = self.file.readline().decode('UTF-8')
               print(linea)
               if linea == '':
                   break
           self.file.close()


   def accion_botonBuscar(self):


       self.datosCorrectos = True


       self.ventanaDialogo.setWindowTitle("Buscar las preguntas de validacion")


       if (
               self.documento.text() == ''
       ):
           self.datosCorrectos = False


           self.mensaje.setText("Si va a buscar las preguntas"
                                " para recuperar la contraseña."
                                "\nDebe primero, ingresar el documento.")


           self.ventanaDialogo.exec_()


       if (
               not self.documento.text().isnumeric()
       ):
           self.datosCorrectos = False


           self.mensaje.setText("El documento debe ser numerico."
                                "\nNo ingrese letras"
                                " ni caracteres especiales.")


           self.ventanaDialogo.exec_()


           self.documento.setText(' ')


       if (
               self.datosCorrectos
       ):


           self.file = open('datos/clientes.txt', 'rb')


           usuarios = []


           while self.file:
               linea = self.file.readline().decode('UTF-8')
               lista = linea.split(";")


               if linea == '':
                   break


               u = Cliente(
                   lista[0],
                   lista[1],
                   lista[2],
                   lista[3],
                   lista[4],
                   lista[5],
                   lista[6],
                   lista[7],
                   lista[8],
                   lista[9],
                   lista[10],
               )


               usuarios.append(u)


           self.file.close()




           existeDocumento = False


           for u in usuarios:


               if u.documento == self.documento.text():


                   self.pregunta1.setText(u.pregunta1)
                   self.pregunta2.setText(u.pregunta2)
                   self.pregunta3.setText(u.pregunta3)


                   existeDocumento = True


                   break


           if (
                   not existeDocumento
           ):


               self.mensaje.setText("No existe un usuario con este documento:\n"
                                    + self.documento.text())


               self.ventanaDialogo.exec_()


   def accion_botonRecuperar(self):


       self.datosCorrectos = True


       self.ventanaDialogo.setWindowTitle("Recuperar contraseña")


       if (
               self.pregunta1.text() == '' or
               self.pregunta2.text() == '' or
               self.pregunta3.text() == ''


       ):
           self.datosCorrectos = False


           self.mensaje.setText("Para recuperar la contraseña debe buscar las"
                                "\npreguntas de verificacion. Primero ingrese su"
                                "\ndocumento y luego presione el boton 'Buscar'")


           self.ventanaDialogo.exec_()


       if (
           self.pregunta1.text() != '' and
           self.respuesta1.text() == '' and
           self.pregunta2.text() != '' and
           self.respuesta2.text() == '' and
           self.pregunta3.text() != '' and
           self.respuesta3.text() == ''
       ):
           self.datosCorrectos = False


           self.mensaje.setText("Para recuperar la contraseña debe ingresar"
                                "\nlas respuestas a cada pregunta.")


           self.ventanaDialogo.exec_()


       if (
           self.datosCorrectos
       ):
           self.file = open('datos/clientes.txt', 'rb')


           usuarios = []


           while self.file:
               linea = self.file.readline().decode('UTF-8')
               lista = linea.split(";")


               if linea == '':
                   break


               u = Cliente(
                   lista[0],
                   lista[1],
                   lista[2],
                   lista[3],
                   lista[4],
                   lista[5],
                   lista[6],
                   lista[7],
                   lista[8],
                   lista[9],
                   lista[10],
               )


               usuarios.append(u)


           self.file.close()


           existeDocumento = False


           resp1 = ''
           resp2 = ''
           resp3 = ''
           passw = ''


           for u in usuarios:


               if u.documento == self.documento.text():
                   existeDocumento = True


                   resp1 = u.respuesta1
                   resp2 = u.respuesta2
                   resp3 = u.respuesta3
                   passw = u.password


                   break


           if (
                   self.respuesta1.text().lower().strip() == resp1.lower().strip() and
                   self.respuesta2.text().lower().strip() == resp2.lower().strip() and
                   self.respuesta3.text().lower().strip() == resp3.lower().strip()
           ):


               self.accion_botonLimpiar()


               self.mensaje.setText("Contraseña: " + passw)


               self.ventanaDialogo.exec_()
           else:


               self.mensaje.setText("Las respuestas son incorrectas para estas"
                                    "\npreguntas de recuperacion de contraseña."
                                    "\nVuelva a intentarlo.")


               self.ventanaDialogo.exec_()


if __name__ == '__main__':
   app = QApplication(sys.argv)


   ventana1 = Ventana1()


   ventana1.show()


   sys.exit(app.exec_())
