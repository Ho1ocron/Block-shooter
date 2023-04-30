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
        self.button.move(250, 135)
        self.button.clicked.connect(self.start)

        #: statistics button
        self.button1 = QPushButton('Statistics', self)
        self.button1.setFont(QFont('Arial', 35))
        self.button1.setStyleSheet("background-color: rgba(255, 255, 255, 75);\n""border: rgba(255, 255, 255, 100);")
        self.button1.setToolTip('This is an example button')
        self.button1.resize(300, 55)
        self.button1.move(250, 300)
        self.button1.clicked.connect(self.statistics)

        #: shop button
        self.button2 = QPushButton('Shop', self)
        self.button2.setFont(QFont('Arial', 35))
        self.button2.setStyleSheet("background-color: rgba(255, 255, 255, 75);\n""border: rgba(255, 255, 255, 100);")
        self.button2.setToolTip('This is an example button')
        self.button2.resize(300, 55)
        self.button2.move(250, 190)
        self.button2.clicked.connect(self.shop)
        

        # settings button
        self.button3 = QPushButton('Settings', self)
        self.button3.setFont(QFont('Arial', 35))
        self.button3.setStyleSheet("background-color: rgba(255, 255, 255, 75);\n""border: rgba(255, 255, 255, 100);")
        self.button3.setToolTip('This is an example button')
        self.button3.resize(300, 55)
        self.button3.move(250, 245)
        self.button3.clicked.connect(self.settings)

        #: exit button 
        self.button4 = QPushButton('Exit', self)
        self.button4.setFont(QFont('Arial', 35))
        self.button4.setStyleSheet("background-color: rgba(255, 255, 255, 75);\n""border: rgba(255, 255, 255, 100);")
        self.button4.setToolTip('This is an example button')
        self.button4.resize(300, 55)
        self.button4.move(250, 410)
        self.button4.clicked.connect(self.exit)

        #: about game
        self.button5 = QPushButton('About game', self)
        self.button5.setFont(QFont('Arial', 35))
        self.button5.setStyleSheet("background-color: rgba(255, 255, 255, 75);\n""border: rgba(255, 255, 255, 100);")
        self.button5.setToolTip('This is an example button')
        self.button5.resize(300, 55)
        self.button5.move(250, 355)
        self.button5.clicked.connect(self.about_)

        self.list_main_menu = [self.button, self.button1, self.button2, self.button3, self.button4, self.button5]

        #: button play on map
        self.map_btn = QPushButton('Play\non map', self)
        self.map_btn.setFont(QFont('Arial', 35))
        self.map_btn.setStyleSheet("background-color: rgba(255, 255, 255, 75);\n""border: rgba(255, 255, 255, 100);")
        self.map_btn.resize(300, 110)
        self.map_btn.move(250, 150)
        self.map_btn.clicked.connect(self.stand_map)
        self.map_btn.hide()
        
        #: button build map
        self.build_map = QPushButton('Build\nmap', self)
        self.build_map.setFont(QFont('Arial', 35))
        self.build_map.setStyleSheet("background-color: rgba(255, 255, 255, 75);\n""border: rgba(255, 255, 255, 100);") 
        self.build_map.resize(300, 110) 
        self.build_map.move(250, 270) 
        self.build_map.clicked.connect(self.user_map) 
        self.build_map.hide() 

        #: back button
        self.exit_btn = QPushButton('Back', self)
        self.exit_btn.setFont(QFont('Arial', 35))
        self.exit_btn.setStyleSheet("background-color: rgba(255, 255, 255, 75);\n""border: rgba(255, 255, 255, 100);") 
        self.exit_btn.resize(300, 50) 
        self.exit_btn.move(250, 390) 
        self.exit_btn.clicked.connect(self.menu_exit) 
        self.exit_btn.hide() 

        self.list_play_menu = [self.map_btn, self.build_map, self.exit_btn]

        #: standart map choice
        self.map_ch = QPushButton('1st map', self)
        self.map_ch.setFont(QFont('Arial', 35))
        self.map_ch.setStyleSheet("background-color: rgba(255, 255, 255, 75);\n""border: rgba(255, 255, 255, 100);") 
        self.map_ch.resize(300, 110)
        self.map_ch.move(250, 110)
        self.map_ch.clicked.connect(self.play) 
        self.map_ch.hide()

        self.map_ch1 = QPushButton('2nd map', self)
        self.map_ch1.setFont(QFont('Arial', 35))
        self.map_ch1.setStyleSheet("background-color: rgba(255, 255, 255, 75);\n""border: rgba(255, 255, 255, 100);") 
        self.map_ch1.resize(300, 110)
        self.map_ch1.move(250, 230)
        self.map_ch1.clicked.connect(self.play) 
        self.map_ch1.hide() 

        self.map_ch2 = QPushButton('3rd map', self)
        self.map_ch2.setFont(QFont('Arial', 35))
        self.map_ch2.setStyleSheet("background-color: rgba(255, 255, 255, 75);\n""border: rgba(255, 255, 255, 100);") 
        self.map_ch2.resize(300, 110)
        self.map_ch2.move(250, 350)
        self.map_ch2.clicked.connect(self.play) 
        self.map_ch2.hide()  

        self.map_exit_btn = QPushButton('Back', self)
        self.map_exit_btn.setFont(QFont('Arial', 35))
        self.map_exit_btn.setStyleSheet("background-color: rgba(255, 255, 255, 75);\n""border: rgba(255, 255, 255, 100);") 
        self.map_exit_btn.resize(300, 50) 
        self.map_exit_btn.move(250, 470) 
        self.map_exit_btn.clicked.connect(self.stand_map_exit) 
        self.map_exit_btn.hide() 

        self.stand_map_list = [self.map_ch, self.map_ch1, self.map_ch2, self.map_exit_btn]

        #: standart map choice
        self.map_ch = QPushButton('1st map', self)
        self.map_ch.setFont(QFont('Arial', 35))
        self.map_ch.setStyleSheet("background-color: rgba(255, 255, 255, 75);\n""border: rgba(255, 255, 255, 100);") 
        self.map_ch.resize(300, 110)
        self.map_ch.move(250, 110)
        self.map_ch.clicked.connect(self.play) 
        self.map_ch.hide()

        self.map_ch1 = QPushButton('2nd map', self)
        self.map_ch1.setFont(QFont('Arial', 35))
        self.map_ch1.setStyleSheet("background-color: rgba(255, 255, 255, 75);\n""border: rgba(255, 255, 255, 100);") 
        self.map_ch1.resize(300, 110)
        self.map_ch1.move(250, 230)
        self.map_ch1.clicked.connect(self.play) 
        self.map_ch1.hide() 

        self.map_ch2 = QPushButton('3rd map', self)
        self.map_ch2.setFont(QFont('Arial', 35))
        self.map_ch2.setStyleSheet("background-color: rgba(255, 255, 255, 75);\n""border: rgba(255, 255, 255, 100);") 
        self.map_ch2.resize(300, 110)
        self.map_ch2.move(250, 350)
        self.map_ch2.clicked.connect(self.play) 
        self.map_ch2.hide()  

        self.map_exit_btn = QPushButton('Back', self)
        self.map_exit_btn.setFont(QFont('Arial', 35))
        self.map_exit_btn.setStyleSheet("background-color: rgba(255, 255, 255, 75);\n""border: rgba(255, 255, 255, 100);") 
        self.map_exit_btn.resize(300, 50) 
        self.map_exit_btn.move(250, 470) 
        self.map_exit_btn.clicked.connect(self.stand_map_exit) 
        self.map_exit_btn.hide() 

        self.stand_map_list = [self.map_ch, self.map_ch1, self.map_ch2, self.map_exit_btn]

        #: user map choice
        self.usmap_ch = QPushButton('1st map', self)
        self.usmap_ch.setFont(QFont('Arial', 35))
        self.usmap_ch.setStyleSheet("background-color: rgba(255, 255, 255, 75);\n""border: rgba(255, 255, 255, 100);") 
        self.usmap_ch.resize(300, 110)
        self.usmap_ch.move(250, 110)
        self.usmap_ch.clicked.connect(self.play) 
        self.usmap_ch.hide()

        self.usmap_ch1 = QPushButton('2nd map', self)
        self.usmap_ch1.setFont(QFont('Arial', 35))
        self.usmap_ch1.setStyleSheet("background-color: rgba(255, 255, 255, 75);\n""border: rgba(255, 255, 255, 100);") 
        self.usmap_ch1.resize(300, 110)
        self.usmap_ch1.move(250, 230)
        self.usmap_ch1.clicked.connect(self.play) 
        self.usmap_ch1.hide() 

        self.usmap_ch2 = QPushButton('3rd map', self)
        self.usmap_ch2.setFont(QFont('Arial', 35))
        self.usmap_ch2.setStyleSheet("background-color: rgba(255, 255, 255, 75);\n""border: rgba(255, 255, 255, 100);") 
        self.usmap_ch2.resize(300, 110)
        self.usmap_ch2.move(250, 350)
        self.usmap_ch2.clicked.connect(self.play) 
        self.usmap_ch2.hide()  

        self.usmap_exit_btn = QPushButton('Back', self)
        self.usmap_exit_btn.setFont(QFont('Arial', 35))
        self.usmap_exit_btn.setStyleSheet("background-color: rgba(255, 255, 255, 75);\n""border: rgba(255, 255, 255, 100);") 
        self.usmap_exit_btn.resize(300, 50) 
        self.usmap_exit_btn.move(250, 470) 
        self.usmap_exit_btn.clicked.connect(self.user_map_exit) 
        self.usmap_exit_btn.hide() 

        self.user_map_list = [self.usmap_ch, self.usmap_ch1, self.usmap_ch2, self.usmap_exit_btn]

        """Shop buttons"""

        #: bg picture shop
        self.bg_sh = QPushButton('Backgrounds', self)
        self.bg_sh.setFont(QFont('Arial', 35))
        self.bg_sh.setStyleSheet("background-color: rgba(255, 255, 255, 75);\n""border: rgba(255, 255, 255, 100);") 
        self.bg_sh.resize(300, 55) 
        self.bg_sh.move(250, 175)
        self.bg_sh.clicked.connect(self.bg_buy) 
        self.bg_sh.hide() 

        #: car shop
        self.car_sh = QPushButton('Cars', self)
        self.car_sh.setFont(QFont('Arial', 35))
        self.car_sh.setStyleSheet("background-color: rgba(255, 255, 255, 75);\n""border: rgba(255, 255, 255, 100);") 
        self.car_sh.resize(300, 55) 
        self.car_sh.move(250, 240)
        self.car_sh.clicked.connect(self.car_buy) 
        self.car_sh.hide()
        
        #: map shop
        self.map_sh = QPushButton('Maps', self)
        self.map_sh.setFont(QFont('Arial', 35))
        self.map_sh.setStyleSheet("background-color: rgba(255, 255, 255, 75);\n""border: rgba(255, 255, 255, 100);") 
        self.map_sh.resize(300, 55) 
        self.map_sh.move(250, 305)
        self.map_sh.clicked.connect(self.map_buy) 
        self.map_sh.hide()

        #: exit from shop
        self.shop_exit = QPushButton('Back', self)
        self.shop_exit.setFont(QFont('Arial', 35))
        self.shop_exit.setStyleSheet("background-color: rgba(255, 255, 255, 75);\n""border: rgba(255, 255, 255, 100);") 
        self.shop_exit.resize(300, 55) 
        self.shop_exit.move(250, 370)
        self.shop_exit.clicked.connect(self.shop_exit_func) 
        self.shop_exit.hide()
        
        self.shop_list = [self.car_sh, self.map_sh, self.bg_sh, self.shop_exit]

        """Background shop"""

        #: First background
        self.bg0 = QPushButton('Dark ground', self)
        self.bg0.setFont(QFont('Arial', 35))
        self.bg0.setStyleSheet("background-color: rgba(255, 255, 255, 75);\n""border: rgba(255, 255, 255, 100);") 
        self.bg0.resize(400, 55) 
        self.bg0.move(200, 175)
        #self.bg0.clicked.connect(self.user_map_exit) 
        self.bg0.hide() 

        #: Second background
        self.bg1 = QPushButton('Light background', self)
        self.bg1.setFont(QFont('Arial', 35))
        self.bg1.setStyleSheet("background-color: rgba(255, 255, 255, 75);\n""border: rgba(255, 255, 255, 100);") 
        self.bg1.resize(400, 55) 
        self.bg1.move(200, 240)
        #self.bg1.clicked.connect(self.car_buy) 
        self.bg1.hide()

        #: Third background
        self.bg2 = QPushButton('Cust background', self)
        self.bg2.setFont(QFont('Arial', 35))
        self.bg2.setStyleSheet("background-color: rgba(255, 255, 255, 75);\n""border: rgba(255, 255, 255, 100);") 
        self.bg2.resize(400, 55) 
        self.bg2.move(200, 305)
        #self.bg2.clicked.connect(self.map_buy) 
        self.bg2.hide()

        #: exit from background shop
        self.bg_exit = QPushButton('Back', self)
        self.bg_exit.setFont(QFont('Arial', 35))
        self.bg_exit.setStyleSheet("background-color: rgba(255, 255, 255, 75);\n""border: rgba(255, 255, 255, 100);") 
        self.bg_exit.resize(400, 55) 
        self.bg_exit.move(200, 370)
        self.bg_exit.clicked.connect(self.bg_exit_shop) 
        self.bg_exit.hide()

        self.bg_list = [self.bg0, self.bg1, self.bg2, self.bg_exit]

        """Car shop"""

        #: 1st car
        self.car0 = QPushButton('Dark car', self)
        self.car0.setFont(QFont('Arial', 35))
        self.car0.setStyleSheet("background-color: rgba(255, 255, 255, 75);\n""border: rgba(255, 255, 255, 100);") 
        self.car0.resize(400, 55) 
        self.car0.move(200, 175)
        #self.car0.clicked.connect(self.user_map_exit) 
        self.car0.hide() 

        #: 2nd car
        self.car1 = QPushButton('Light car', self)
        self.car1.setFont(QFont('Arial', 35))
        self.car1.setStyleSheet("background-color: rgba(255, 255, 255, 75);\n""border: rgba(255, 255, 255, 100);") 
        self.car1.resize(400, 55) 
        self.car1.move(200, 240)
        #self.car1.clicked.connect(self.car_buy) 
        self.car1.hide()

        #: 3rd car
        self.car2 = QPushButton('Cust car', self)
        self.car2.setFont(QFont('Arial', 35))
        self.car2.setStyleSheet("background-color: rgba(255, 255, 255, 75);\n""border: rgba(255, 255, 255, 100);") 
        self.car2.resize(400, 55) 
        self.car2.move(200, 305)
        #self.car2.clicked.connect(self.map_buy) 
        self.car2.hide()

        #: exit from car shop
        self.car_exit = QPushButton('Back', self)
        self.car_exit.setFont(QFont('Arial', 35))
        self.car_exit.setStyleSheet("background-color: rgba(255, 255, 255, 75);\n""border: rgba(255, 255, 255, 100);") 
        self.car_exit.resize(400, 55) 
        self.car_exit.move(200, 370)
        self.car_exit.clicked.connect(self.car_exit_shop) 
        self.car_exit.hide()

        self.car_list = [self.car0, self.car1, self.car2, self.car_exit]

        """Map shop"""
        
        #: 1st map
        self.map0 = QPushButton('Dark map', self)
        self.map0.setFont(QFont('Arial', 35))
        self.map0.setStyleSheet("background-color: rgba(255, 255, 255, 75);\n""border: rgba(255, 255, 255, 100);") 
        self.map0.resize(400, 55) 
        self.map0.move(200, 175)
        #self.map0.clicked.connect(self.user_map_exit) 
        self.map0.hide() 

        #: 2nd map
        self.map1 = QPushButton('Light map', self)
        self.map1.setFont(QFont('Arial', 35))
        self.map1.setStyleSheet("background-color: rgba(255, 255, 255, 75);\n""border: rgba(255, 255, 255, 100);") 
        self.map1.resize(400, 55) 
        self.map1.move(200, 240)
        #self.map1.clicked.connect(self.car_buy) 
        self.map1.hide()

        #: 3rd map
        self.map2 = QPushButton('Cust map', self)
        self.map2.setFont(QFont('Arial', 35))
        self.map2.setStyleSheet("background-color: rgba(255, 255, 255, 75);\n""border: rgba(255, 255, 255, 100);") 
        self.map2.resize(400, 55) 
        self.map2.move(200, 305)
        #self.map2.clicked.connect(self.map_buy) 
        self.map2.hide()

        #: exit from map shop
        self.map_exit = QPushButton('Back', self)
        self.map_exit.setFont(QFont('Arial', 35))
        self.map_exit.setStyleSheet("background-color: rgba(255, 255, 255, 75);\n""border: rgba(255, 255, 255, 100);") 
        self.map_exit.resize(400, 55) 
        self.map_exit.move(200, 370)
        self.map_exit.clicked.connect(self.map_exit_shop) 
        self.map_exit.hide()

        self.map_list = [self.map0, self.map1, self.map2, self.map_exit]

        self.show()
    

    @pyqtSlot()
    def play(self):
        #self.palette.setBrush(QPalette.Background, QBrush(QPixmap("img.jpeg")))
        #self.setPalette(self.palette)
        launch = threading.Timer(1, self.game)
        launch.start()



    #: Menu forward navigation
    def start(self):
        for i in self.list_main_menu:
            i.hide()

        for j in self.list_play_menu:
            j.show()


    #: shop navigation
    def shop(self):
        for i in self.list_main_menu:
            i.hide()
       
        for j in self.shop_list:
            j.show()
    
    def bg_buy(self):
        for i in self.shop_list:
            i.hide()
        
        for j in self.bg_list:
            j.show()

    def car_buy(self):
        for i in self.shop_list:
            i.hide()
        
        for j in self.car_list:
            j.show()
    
    def map_buy(self):
        for i in self.shop_list:
            i.hide()
        
        for j in self.map_list:
            j.show()


    def settings(self):
        #self.button3.deleteLater()
        #self.button3.hide()
        print('Set me up please!')
    


    def statistics(self):
        #print(os.getpid())
        print("Victory - 65% ")
    


    def about_(self):
        print(os.get_exec_path())
    

    #map navigation
    def stand_map(self):
        for i in self.list_play_menu:
            i.hide()
        
        for j in self.stand_map_list:
            j.show()
    
    def user_map(self):
        for i in self.list_play_menu:
            i.hide()
        
        for j in self.user_map_list:
            j.show()



    #: Menu exit navigatoin
    def exit(self):
        sys.exit()


    def menu_exit(self):
        for i in self.list_main_menu:
            i.show()

        for j in self.list_play_menu:
            j.hide()
    

    def stand_map_exit(self):
        for i in self.list_play_menu:
            i.show()
        
        for j in self.stand_map_list:
            j.hide()
    

    def user_map_exit(self):
        for i in self.list_play_menu:
            i.show()
        
        for j in self.user_map_list:
            j.hide()
    

    def shop_exit_func(self):
        for i in self.list_main_menu:
            i.show()
        
        for j in self.shop_list:
            j.hide()
        
    
    def bg_exit_shop(self):
        for i in self.bg_list:
            i.hide()
        
        for j in self.shop_list:
            j.show()
    
    
    def car_exit_shop(self):
        for i in self.car_list:
            i.hide()
        
        for j in self.shop_list:
            j.show()
    
    def map_exit_shop(self):
        for i in self.map_list:
            i.hide()
        
        for j in self.shop_list:
            j.show()



    def game(self):
        os.system("python New_game.py 1")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())