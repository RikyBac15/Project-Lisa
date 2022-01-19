import sys
import time
from PyQt5.QtWidgets import (QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout, QMainWindow, QDesktopWidget)
from PyQt5.QtGui import QPixmap, QCursor, QMovie
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import QCoreApplication, Qt, QPropertyAnimation
from PyQt5.QtCore import pyqtSignal as Signal

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Window size
        self.setFixedSize(400, 1017)

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
        '''
        self.animation = QLabel(self)
        #movie = QMovie("Assets/Lisa_animation_transparent.gif")
        movie = QMovie("Assets/Lisa_animation_V3_rev2.gif")
        #movie = QMovie("Assets/Lisa_animation_V2.gif")
        self.animation.setMovie(movie)
        #animation.setMovie(self.movie)
        #animation.setAlignment(QtCore.Qt.AlignCenter)
        #animation.setStyleSheet("margin-top: 100px;")
        #self.animation.setMovie(movie)
        #self.animation.move(160, 60)
        self.animation.setGeometry(155,55,90,90)
        #self.animation.setGeometry(160,60,80,80)
        #self.animation.setGeometry(100,70,200,56)
        movie.start()'''

        self.button = QPushButton('', self)
        self.button.setGeometry(173, 65, 55, 70)
        self.button.clicked.connect(self.clickme)
        self.button.setStyleSheet("background-color: #353535; background-image : url(Assets/Microphone_icon_little.png); border-radius: 22px")

        #time.sleep(5)
        #self.animation.hide()
        #WikiWindow()

        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def clickme(self):
        #self.animation.hide()
        self.resizeMainWindow(400, 400)
        self.button.hide()
        self.animation = QLabel(self)
        movie = QMovie("Assets/Lisa_animation_V3_rev2.gif")
        self.animation.setMovie(movie)
        self.animation.setGeometry(155,55,90,90)
        movie.start()
        self.animation.show()

        print("pressed")

    def WikiWindow(self):
        self.resizeMainWindow(400, 400)
        #self.centralwidget.resize(400, HEIGHT)

    def resizeMainWindow(self, width, height):
        self.animation = QPropertyAnimation(self.centralwidget, b"size")
        self.animation.setDuration(1000)
        self.animation.setEndValue(QtCore.QSize(width, height))
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
        self.animation.start()

app = QApplication(sys.argv)
#window = QWidget()
app.setStyleSheet("QMainWindow{background-color: #353535; border: 1px solid black;}") # border-radius: 22px;
#window.setLayout(grid)
Window = MainWindow()
sys.exit(app.exec())