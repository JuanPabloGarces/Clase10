import sys

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QVBoxLayout, QApplication, QWidget, QGridLayout, \
    QButtonGroup, QPushButton, QScrollArea

from PyQt5 import QtGui

from cliente import Cliente

import math

from ventana3 import Ventana3


class Ventana2(QMainWindow):

    def __init__(self, anterior):
        super(Ventana2, self).__init__(anterior)

        self.ventanaAnterior = anterior

        self.setWindowTitle("Usuarios Registrados")

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

        self.imagenFondo = QPixmap("imagenes/fondo.2.jpg")

        self.fondo.setPixmap(self.imagenFondo)

        self.fondo.setScaledContents(True)

        self.resize(self.imagenFondo.width(), self.imagenFondo.height())

        self.setCentralWidget(self.fondo)

        self.vertical = QVBoxLayout()

        self.letrero1 = QLabel()

        self.letrero1.setText("Usuarios Registrados")

        self.letrero1.setFont(QFont("Andale Mono", 20))

        self.letrero1.setStyleSheet("color: #000080;")

        self.vertical.addWidget(self.letrero1)

        self.vertical.addStretch()

        self.scrollArea = QScrollArea()

        self.scrollArea.setStyleSheet("background-color: #00FF0000;")

        self.scrollArea.setWidgetResizable(True)

        self.contenedora = QWidget()

        self.cuadricula = QGridLayout(self.contenedora)

        self.scrollArea.setWidget(self.contenedora)

        self.vertical.addWidget(self.scrollArea)

        self.file = open('datos/clientes.txt', 'rb')

        self.usuarios = []


        self.file.close()

        self.numeroUsuarios = len(self.usuarios)

        self.contador = 0

        self.elementosPorColumna = 3

        self.numeroFilas = math.ceil(self.numeroUsuarios / self.elementosPorColumna) + 1

        self.botones = QButtonGroup()

        self.botones.setExclusive(False)

        for fila in range(1, self.numeroFilas):
            for columna in range(1, self.elementosPorColumna+1):

                if self.contador < self.numeroUsuarios:

                    self.ventanaAuxiliar = QWidget

                    self.ventanaAuxiliar.setFixedHeight(100)
                    self.ventanaAuxiliar.setFixedWidth(200)

                    self.verticalCuadricula = QVBoxLayout()

                    self.botonAccion = QPushButton(self.usuarios[self.contador].documento)

                    self.botonAccion.setFixedWidth(150)

                    self.botonAccion.setStyleSheet("background-color: #008B45;"
                                                   "color: #FFFFFF;"
                                                   "padding: 10px"
                                                   )

                    self.verticalCuadricula.addWidget(self.botonAccion)

                    self.botones.addButton(self.botonAccion, int(self.usuarios[self.contador].documento))

                    self.verticalCuadricula.addStretch()

                    self.ventanaAuxiliar.setLayout(self.verticalCuadricula)

                    self.cuadricula.addWidget(self.ventanaAuxiliar, fila, columna)

                    self.contador = +1

        self.botones.idClicked.connect(self.metodo_accionBotones)

        self.botonFormaTabular = QPushButton("Forma Tabular")

        self.botonFormaTabular.setFixedWidth(100)

        self.botonFormaTabular.setStyleSheet("background-color: #008B45;"
                                             "color: #FFFFFF;"
                                             "padding: 10px;"
                                             "margi-top: 10px"
                                             )
        self.botonFormaTabular.clicked.connect(self.metodo_botonFormaTabular)

        self.vertical.addWidget(self.botonFormaTabular)

        self.botonVolver = QPushButton("Volver")

        self.botonVolver.setStyleSheet("background-color: #008B45;"
                                       "color: #FFFFFF;"
                                       "padding: 10px;"
                                       )

        self.botonVolver.clicked.connect(self.metodo_botonVolver)

        self.vertical.addWidget(self.botonVolver)

        self.fondo.setLayout(self.vertical)

    def metodo_accionBotones(self, cedulaUsuario):
        print(cedulaUsuario)

    def metodo_botonVolver(self):
         self.hide()
         self.ventanaAnterior.show

    def metodo_botonFormaTabular(self):
        self.hide()
        self.ventana3 = Ventana3(self)
        self.ventana3.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)

    ventana2 = Ventana2()

    ventana2.show()

    sys.exit(app.exec_())

