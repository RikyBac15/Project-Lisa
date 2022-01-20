import sys
import time
from PyQt5.QtWidgets import (QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout, QMainWindow, QDesktopWidget)
from PyQt5.QtGui import QPixmap, QCursor, QMovie
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import QCoreApplication, Qt, QPropertyAnimation, QSize, QTime, QTimer, QEventLoop
from PyQt5.QtCore import pyqtSignal as Signal

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Window size
        self.setFixedSize(400, 980)

        # Widget
        self.centralwidget = QWidget(self)
        self.centralwidget.resize(400, 150)
        
        #self.mwidget = QMainWindow(self)
        
        # Initial
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowOpacity(0.6)

        radius = 30
        self.centralwidget.setStyleSheet(
            """
            background:#353535;
            border-top-left-radius:{0}px;
            border-bottom-left-radius:{0}px;
            border-top-right-radius:{0}px;
            border-bottom-right-radius:{0}px;
            """.format(radius)
        )

        self.center()
        #self.MainWindow.move(960,500)

        self.label = QLabel(self)
        self.label.setText("Ciao, cosa posso fare per te?")
        self.label.setStyleSheet("background-color: #353535;""border: 1px #353535;""color: #B470DD;""font: bold 15pt 'Product Sans';")
        self.label.setGeometry(35,15,350,40)

        self.button = QPushButton('', self)
        self.button.setGeometry(173, 65, 55, 70)
        self.button.clicked.connect(self.clickme)
        self.button.setStyleSheet("background-color: #353535; background-image : url(Assets/Microphone_icon_little.png); border-radius: 22px")

        self.show()

    def WikiWindow(self, image, text):
        self.animation.hide()
        self.label.setText("Ecco cosa ho trovato:")
        self.resizeMainWindow(400, 400)
        loop = QEventLoop()
        QTimer.singleShot(1000, loop.quit)
        loop.exec_()
        self.pixmap = QLabel(self)
        #self.picture = QPixmap(image)
        #self.pixmap.setPixmap(self.picture.scaled(340, 200, QtCore.Qt.KeepAspectRatio))
        self.pixmap.setGeometry(30,60,340,191)
        self.pixmap.setStyleSheet("border-image: url(Assets/Test2.jpg); background-color: #353535; border-radius: 22px;")
        self.pixmap.show()
        
        self.informations = QLabel(self)
        self.informations.setText(text)
        self.informations.setStyleSheet("background-color: #353535;""border: 1px #353535;""color: #FFFFFF;""font: bold 10.8pt 'Product Sans';")
        self.informations.setAlignment(QtCore.Qt.AlignLeft)
        self.informations.setGeometry(30,272,348,100)
        self.informations.setWordWrap(True)
        self.informations.show()
        

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def clickme(self):
        self.button.hide()
        self.animation = QLabel(self)
        movie = QMovie("Assets/Lisa_animation_V3_rev2.gif")
        self.animation.setMovie(movie)
        self.animation.setGeometry(155,55,90,90)
        movie.start()
        self.animation.show()
        
        self.WikiWindow("Assets/Test.jpg", "Barack Hussein Obama II (/bəˈrɑːk hʊˈseɪn oʊˈbɑːmə/, pronuncia[?·info]; Honolulu, 4 agosto 1961) è un politico statunitense, 44º presidente degli Stati Uniti d'America dal 2009 al 2017, prima persona di origini afroamericane a ricoprire tale carica. " )

        print("pressed")

    def resizeMainWindow(self, WIDTH, HEIGHT):
        self.animation = QPropertyAnimation(self.centralwidget, b"size")
        self.animation.setDuration(750)
        self.animation.setEndValue(QtCore.QSize(WIDTH, HEIGHT))
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
        self.animation.start()

app = QApplication(sys.argv)
app.setStyleSheet("QMainWindow{background-color: #353535; border: 1px solid black;}") # border-radius: 22px;
Window = MainWindow()
sys.exit(app.exec())