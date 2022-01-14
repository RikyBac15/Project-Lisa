import sys
from PyQt5.QtWidgets import (QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout, QMainWindow, QDesktopWidget)
from PyQt5.QtGui import QPixmap, QCursor, QMovie
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import QCoreApplication, Qt

class lisa_gui(QMainWindow):
    def __init__(self):
        super().__init__()

        self.mwidget = QMainWindow(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.setFixedSize(400, 150)
        self.center()

        self.label = QLabel(self)
        self.label.setText("Ciao, cosa posso fare per te?")
        self.label.setStyleSheet("background-color: #353535;""border: 1px #353535;""color: #FFFFFF;""font: bold 15pt 'Product Sans';")
        self.label.setGeometry(30,10,350,40)
        
        animation = QLabel()
        movie = QMovie("Animations/Lisa_animation_transparent.gif")
        animation.setMovie(movie)
        #animation.setMovie(self.movie)
        #animation.setAlignment(QtCore.Qt.AlignCenter)
        #animation.setStyleSheet("margin-top: 100px;")
        #self.animation.setMovie(movie)
        animation.move(0, 0)
        #animation.setGeometry(160,60,80,80)
        movie.start()

        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

app = QApplication(sys.argv)
#window = QWidget()
#window.setFixedWidth(400)
app.setStyleSheet("QMainWindow{background-color: #353535; border: 1px solid black;}") # border-radius: 22px;

ex = lisa_gui()
sys.exit(app.exec())