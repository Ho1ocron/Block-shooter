import os
import sys
import New_game
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QPalette, QBrush, QPixmap
from PyQt5.QtGui import QPalette
from PyQt5.QtGui import QFont
from PyQt5.QtCore import pyqtSlot
import threading


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Cold Road Alpha 0.1'
        self.left = 760
        self.top = 200
        self.width = 800
        self.height = 600
        self.initUI()

    def initUI(self):
        
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap("back.png")))
        self.setPalette(self.palette)

        #: start button
        self.button = QPushButton('Start', self)
        self.button.setFont(QFont('Arial', 35))
        self.button.setStyleSheet("background-color: rgba(255, 255, 255, 75);\n""border: rgba(255, 255, 255, 100);")
        self.button.setToolTip('This is an example button')
        self.button.resize(300, 55)
        self.button.move(250, 165)
        self.button.clicked.connect(self.start)

        #: statistics button
        self.button1 = QPushButton('Statistics', self)
        self.button1.setFont(QFont('Arial', 35))
        self.button1.setStyleSheet("background-color: rgba(255, 255, 255, 75);\n""border: rgba(255, 255, 255, 100);")
        self.button1.setToolTip('This is an example button')
        self.button1.resize(300, 55)
        self.button1.move(250, 330)
        self.button1.clicked.connect(self.statistics)

        #: shop button
        self.button2 = QPushButton('Shop', self)
        self.button2.setFont(QFont('Arial', 35))
        self.button2.setStyleSheet("background-color: rgba(255, 255, 255, 75);\n""border: rgba(255, 255, 255, 100);")
        self.button2.setToolTip('This is an example button')
        self.button2.resize(300, 55)
        self.button2.move(250, 220)
        self.button2.clicked.connect(self.shop)
        

        # special button
        self.button3 = QPushButton('Settings', self)
        self.button3.setFont(QFont('Arial', 35))
        self.button3.setStyleSheet("background-color: rgba(255, 255, 255, 75);\n""border: rgba(255, 255, 255, 100);")
        self.button3.setToolTip('This is an example button')
        self.button3.resize(300, 55)
        self.button3.move(250, 275)
        self.button3.clicked.connect(self.settings)

        #: exit button 
        self.button4 = QPushButton('Exit', self)
        self.button4.setFont(QFont('Arial', 35))
        self.button4.setStyleSheet("background-color: rgba(255, 255, 255, 75);\n""border: rgba(255, 255, 255, 100);")
        self.button4.setToolTip('This is an example button')
        self.button4.resize(300, 55)
        self.button4.move(250, 440)
        self.button4.clicked.connect(self.exit)

        #: about game
        self.button5 = QPushButton('About game', self)
        self.button5.setFont(QFont('Arial', 35))
        self.button5.setStyleSheet("background-color: rgba(255, 255, 255, 75);\n""border: rgba(255, 255, 255, 100);")
        self.button5.setToolTip('This is an example button')
        self.button5.resize(300, 55)
        self.button5.move(250, 385)
        self.button5.clicked.connect(self.about_)


        self.list_main_menu = [self.button, self.button1, self.button2, self.button3, self.button4, self.button5]

        #: button play on map
        self.map_btn = QPushButton('Play\non map', self)
        self.map_btn.setFont(QFont('Arial', 35))
        self.map_btn.setStyleSheet("background-color: rgba(255, 255, 255, 75);\n""border: rgba(255, 255, 255, 100);")
        self.map_btn.resize(200, 110)
        self.map_btn.move(300, 110)
        self.map_btn.clicked.connect(self.play)
        self.map_btn.hide()
        
        #: button build map
        self.build_map = QPushButton('Build\nmap', self)
        self.build_map.setFont(QFont('Arial', 35))
        self.build_map.setStyleSheet("background-color: rgba(255, 255, 255, 75);\n""border: rgba(255, 255, 255, 100);") 
        self.build_map.resize(200, 110) 
        self.build_map.move(300, 240) 
        self.build_map.clicked.connect(self.play) 
        self.build_map.hide() 

        #: exit button
        self.exit_btn = QPushButton('Back', self)
        self.exit_btn.setFont(QFont('Arial', 35))
        self.exit_btn.setStyleSheet("background-color: rgba(255, 255, 255, 75);\n""border: rgba(255, 255, 255, 100);") 
        self.exit_btn.resize(200, 50) 
        self.exit_btn.move(300, 370) 
        self.exit_btn.clicked.connect(self.menu_exit) 
        self.exit_btn.hide() 

        self.list_play_menu = [self.map_btn, self.build_map, self.exit_btn]

        self.show()
    
    @pyqtSlot()
    def start(self):
        for i in self.list_main_menu:
            i.hide()

        for j in self.list_play_menu:
            j.show()

    @pyqtSlot()
    def play(self):
        #self.palette.setBrush(QPalette.Background, QBrush(QPixmap("img.jpeg")))
        #self.setPalette(self.palette)
        launch = threading.Timer(1, self.game)
        launch.start()

    @pyqtSlot()
    def statistics(self):
        #print(os.getpid())
        print("Victory - 65% ")

    @pyqtSlot()
    def shop(self):
        #self.button3.show()
        print('What do u want to buy?')

    @pyqtSlot()
    def settings(self):
        #self.button3.deleteLater()
        #self.button3.hide()
        print('Set me up please!')
    
    @pyqtSlot()
    def about_(self):
        print(os.get_exec_path())

    @pyqtSlot()
    def exit(self):
        sys.exit()

    @pyqtSlot()
    def menu_exit(self):
        for i in self.list_main_menu:
            i.show()

        for j in self.list_play_menu:
            j.hide()

    def game(self):
        os.system("python New_game.py 1")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
